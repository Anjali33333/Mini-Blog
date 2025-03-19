from django import forms
from .models import Post
from django.utils import timezone
from datetime import timedelta

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_at', 'expires_at']
        widgets = {
            'published_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'expires_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        published_at = cleaned_data.get('published_at')
        expires_at = cleaned_data.get('expires_at')

        if published_at and published_at < timezone.now():
            self.add_error('published_at', 'Published date cannot be in the past')

        if expires_at and published_at and expires_at <= published_at:
            self.add_error('expires_at', 'Expiration date must be after published date')

        return cleaned_data
