from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_draft = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def is_published(self):
        if not self.is_draft and self.published_at:
            return self.published_at <= timezone.now()
        return False

    def is_expired(self):
        if self.expires_at:
            return self.expires_at <= timezone.now()
        return False

    def save(self, *args, **kwargs):
        if self.published_at and self.published_at <= timezone.now():
            self.is_draft = False
        if self.expires_at and self.expires_at <= timezone.now():
            self.is_deleted = True
        super().save(*args, **kwargs)
