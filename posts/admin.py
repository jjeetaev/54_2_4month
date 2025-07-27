from django.contrib import admin
from posts.models import Post, Tag, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at", "updated_at", "rate", "category"]
    list_display_links = ["title", "content", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at", "category", "tags"]
    list_editable = ["rate", "category"]
    list_per_page = 6

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]