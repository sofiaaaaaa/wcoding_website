# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Post

from modeltranslation.admin import TranslationAdmin


class PostAdmin(TranslationAdmin):
    list_display = ('category','title', 'slug', 'author', 'publish', 'status')
    list_display_links = ['title']
    list_filter = ('category', 'status', 'created', 'publish', 'author')
    list_editable = ('category', 'status', 'slug')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    save_as = True

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Post, PostAdmin)

