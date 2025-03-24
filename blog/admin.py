from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post, Profile, Comment

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_select_related = ('profile',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('title', 'content')
    ordering = ('-date_posted',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'post', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('content', 'author__username')
    ordering = ('-date_posted',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
