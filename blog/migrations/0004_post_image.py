# Generated by Django 5.0.2 on 2025-03-24 12:05

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_expires_at_remove_post_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.user_directory_path),
        ),
    ]
