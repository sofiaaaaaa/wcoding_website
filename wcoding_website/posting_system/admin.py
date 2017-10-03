from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'author', 'publish', 'status']
    list_display_links = ['title']
    list_filter = ['category', 'status', 'created', 'publish', 'author']
    list_editable = ['category', 'status', 'slug']
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)
