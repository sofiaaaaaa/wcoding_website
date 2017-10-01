from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model  # for django 1.11
# from django.conf import settings - before django 1.11

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# model managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# Category
class Category(models.Model):
    name = models.CharField(
        max_length=200,
        db_index=True,
        help_text="Short descriptive name for this categroy."
    )

    slug = models.SlugField(
        max_length=200,
        db_index=True,
        unique=True,
        help_text="Short descriptive unique name for use in urls"
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


# Post
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)

    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'
    )
    author = models.ForeignKey(
        get_user_model(),
        related_name='posts'
    )  # django 1.11
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_posts') # before django 1.11
    # body = models.TextField()
    # body = RichTextField()

    body = RichTextUploadingField()

    publish = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    objects = models.Manager()  # The default manager : This is optional, and if you don't specific, the default name is 'objects'!!!

    published = PublishedManager()  # Our custom manager.

    # category
    category = models.ForeignKey(
        Category,
        related_name='posts'
    )

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



