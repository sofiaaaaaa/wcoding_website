from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model  # django 1.11
# from django.conf import settings # before django 1.11

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from taggit.managers import TaggableManager


# model managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(get_user_model(), related_name='blog_posts')  # django 1.11
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_posts') # before django 1.11
    # body = models.TextField()
    # body = RichTextField()
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    object = models.Manager() # The default manager
    published = PublishedManager() # Our custom manager.

    # from taggit
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('posting_system:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    class Meta:
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
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
