# Generated by Django 5.0.2 on 2025-03-24 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='expires_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_at',
        ),
    ]
