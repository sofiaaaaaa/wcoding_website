# -*- coding: utf-8 -*-

from django.views.generic import ListView, TemplateView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from taggit.models import Tag

from .models import Post, Comment

from .forms import EmailPostForm, CommentForm


# Class Based View
class PostListView(ListView):
    model = Post
    template_name = 'wcoding/post/list.html'


class NewsListView(ListView):
    model = Post
    template_name = 'wcoding/post/newsList.html'


# Function View
def post_list(request):
    posts = Post.published.all()

    fulltime_course = posts.filter(category='fulltime_course')

    parttime_course = posts.filter(category='parttime_course')

    camps = posts.filter(category='camp')

    best_picks = posts.filter(category='best_picks')

    meet_the_teams = posts.filter(category='meet_the_team')

    return render(request, 'wcoding/index.html', {'fulltime_course': fulltime_course,
                                                  'parttime_course': parttime_course,
                                                  'camps': camps,
                                                  'best_picks': best_picks,
                                                  'meet_the_teams': meet_the_teams})


def post_detail(request, year, month, day, post):
    # get_object_or_404 : To retrieves the object that matches with the given parameters,
    # or lanuches an HTTP 404(Not found) exception if no object is found.
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'wcoding/post/detail.html', {'post': post,
                                                        'comments': comments,
                                                        'comment_form': comment_form})


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data # This attribute is a dictionary of form fields of form fields and their values.
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
            # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'wcoding/post/share.html', {'post': post, 'form': form, 'sent': sent})
