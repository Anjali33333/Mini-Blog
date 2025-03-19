from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'expires_at', 'is_draft', 'is_deleted')
    list_filter = ('is_draft', 'is_deleted', 'published_at', 'expires_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_at'
    ordering = ('-created_at',)
