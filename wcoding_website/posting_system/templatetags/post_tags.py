from django import template
from django.db.models import Count

from ..models import Post

register = template.Library()

@register.assignment_tag
def show_fulltime_course(count=1):
    posts = Post.published.all()

    return posts.filter(category='fulltime_course')[:count]


@register.assignment_tag
def show_parttime_course(count=1):
    posts = Post.published.all()

    return posts.filter(category='parttime_course')[:count]


@register.assignment_tag
def show_camps(count=1):
    posts = Post.published.all()

    return posts.filter(category='camp')[:count]


@register.assignment_tag
def show_best_picks(count=4):
    posts = Post.published.all()

    return posts.filter(category='best_picks')[:count]


@register.assignment_tag
def show_main_windows(count=3):
    posts = Post.published.all()

    return posts.filter(category='main_window')[:count]


@register.assignment_tag
def show_meet_the_teams(count=1):
    posts = Post.published.all()

    return posts.filter(category='meet_the_team')[:count]


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('wcoding/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# @register.assignment_tag
# def get_most_commented_posts(count=5):
#     return Post.published.annotate(
#         total_comments=Count('comments')
#     ).order_by('-total_comments')[:count]
