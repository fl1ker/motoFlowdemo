from django.contrib import admin
from .models import BlogContent, Blog, BlogImage

@admin.register(BlogContent)
class BlogContentAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "created_at")
    search_fields = ("title", "author_name")
    list_filter = ("created_at",)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("blog_content", "comments")
    search_fields = ("blog_content__title",)

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ("blog_content", "file", "uploaded_at")
    search_fields = ("blog_content__title",)
