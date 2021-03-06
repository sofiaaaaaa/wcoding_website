# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model  # for django 1.11
# from django.conf import settings - before django 1.11

# for translate
from django.utils.translation import ugettext_lazy as _

# CKEditor model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from taggit.managers import TaggableManager


# model managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# Post
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
    )

    CATEGORY_CHOICES = (
        ('main_window', 'Main window'),
        ('meet_the_team', 'Meet the team'),
        ('fulltime_course', 'Fulltime course'),
        ('parttime_course', 'Parttime course'),
        ('camp', 'Camp'),
        ('best_picks', 'Best picks'),
        ('news_events', 'News events'),
    )

    # category
    category = models.CharField(
        _('Category'),
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='classes'
    )

    title = models.CharField(
        _('Title'),
        max_length=250
    )

    slug = models.SlugField(
        _('Slug'),
        max_length=250,
        unique_for_date='publish'
    )

    author = models.ForeignKey(
        get_user_model(),
        related_name='blog_posts',
        verbose_name=_('Author')
    )  # django 1.11
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_posts') # before django 1.11

    thumbnail_image = models.ImageField(
        upload_to='thumbnail/%Y/%m/%d',
        blank=True,
        verbose_name=_('Thumbnail Image')
    )

    # CKEditor    # body = models.TextField(): Basic Django model type
    # body = RichTextField(): Without Image upload
    body = RichTextUploadingField(_('Body'))

    publish = models.DateTimeField(_('Publish'), default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        _('Status'),
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    # Manager
    objects = models.Manager()  # The default manager : This is optional, and if you don't specific, the default name is 'objects'!!!
    published = PublishedManager()  # Our custom manager.

    # from taggit
    tags = TaggableManager(blank=True)

    # Canonical URLs for models
    def get_absolute_url(self):
        return reverse('posting_system:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),  # strftime(): how to format about related to time
                             self.publish.strftime('%d'),
                             self.slug])

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

        # To sort results by the publish field in descending order by default when we query the database.
        # negative prefix is descending order
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
