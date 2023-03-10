# Generated by Django 4.1.5 on 2023-02-16 23:49

from django.db import migrations


def migrate_author_to_contributor(apps, shema_editor):
    Blog = apps.get.model('blogs', 'Blogs')
    for blog in Blog.objects.all():
        if blog.author:
            blog.contributors.add(blog.author, through_defaults ={'contribution': 'auteur principale'})
    


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogcontributor_blog_contributors'),
    ]

    operations = [
    ]
