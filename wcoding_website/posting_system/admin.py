# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Post

# django-parler
from parler.admin import TranslatableAdmin


class PostAdmin(TranslatableAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

