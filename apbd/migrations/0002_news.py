# Generated by Django 5.2.1 on 2025-06-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apbd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='news_images/')),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
