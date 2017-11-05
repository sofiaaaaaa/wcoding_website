# -*- coding: utf-8 -*-

from django import template
from django.db.models import Count

from ..models import Post

register = template.Library()


@register.assignment_tag
def show_all_programs():
    posts = Post.published.all()

    return posts.exclude(category='news_events').exclude(category='meet_the_team').exclude(category='main_window')


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


@register.assignment_tag
def show_latest_news_events():
    posts = Post.published.all()

    return posts.filter(category='news_events')


@register.assignment_tag
def show_past_news_events():
    posts = Post.published.order_by('publish')

    return posts.filter(category='news_events')


@register.simple_tag
def total_posts():

    return Post.published.count()


@register.inclusion_tag('wcoding/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]

    return {'latest_posts': latest_posts}
