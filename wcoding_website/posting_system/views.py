from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


# Class Based View
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'wcoding/post/list.html'


# Function View
def post_list(request):
    posts = Post.published.all()

    regular_class = posts.filter(category='regular_class')

    classes = posts.filter(category='classes')

    camps = posts.filter(category='camp')

    best_picks = posts.filter(category='best_picks')

    return render(request, 'wcoding/index.html', {'regular_class': regular_class,
                                                  'classes': classes,
                                                  'camps': camps,
                                                  'best_picks': best_picks})


def post_detail(request, year, month, day, post):
    # get_object_or_404 : To retrieves the object that matches with the given parameters,
    # or lanuches an HTTP 404(Not found) exception if no object is found.
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'wcoding/post/detail.html', {'post': post})
