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


""" Function View
def post_list(request):
    posts = Post.published.all()
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'wcoding/post/list.html', {'page': page, 'posts': posts})
"""


def post_detail(request, year, month, day, post):
    # get_object_or_404 : To retrieves the object that matches with the given parameters,
    # or lanuches an HTTP 404(Not found) exception if no object is found.
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'wcoding/post/detail.html', {'post': post})
