# Generated by Django 5.2.1 on 2025-06-03 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apbd', '0003_news_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
    ]
