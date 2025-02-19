# Generated by Django 5.1.3 on 2024-12-10 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the blog post', max_length=200, verbose_name='Title')),
                ('content', models.TextField(help_text='Main content of the blog post', verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the blog post was created', verbose_name='Created At')),
                ('author_name', models.CharField(help_text='Name of the author of the blog post', max_length=100, verbose_name='Author Name')),
            ],
            options={
                'verbose_name': 'Blog Content',
                'verbose_name_plural': 'Blog Contents',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, help_text='Comments related to the blog post', null=True, verbose_name='Comments')),
                ('blog_content', models.OneToOneField(help_text='Detailed content of the blog', on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blogs.blogcontent', verbose_name='Blog Content')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(help_text='The image file', upload_to='images/', verbose_name='File')),
                ('description', models.TextField(blank=True, help_text='Optional description of the image', null=True, verbose_name='Description')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the image was uploaded', verbose_name='Uploaded At')),
                ('blog_content', models.ForeignKey(help_text='The blog post this image belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blogs.blogcontent', verbose_name='Blog Content')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'abstract': False,
            },
        ),
    ]
