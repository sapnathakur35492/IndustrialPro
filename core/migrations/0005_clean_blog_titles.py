from django.db import migrations
from django.utils.html import strip_tags


def clean_blog_titles(apps, schema_editor):
    Blog = apps.get_model('core', 'Blog')
    for blog in Blog.objects.all():
        cleaned = strip_tags(blog.title or '').strip()
        if cleaned != blog.title:
            blog.title = cleaned
            blog.save(update_fields=['title'])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_blog'),
    ]

    operations = [
        migrations.RunPython(clean_blog_titles, noop),
    ]
