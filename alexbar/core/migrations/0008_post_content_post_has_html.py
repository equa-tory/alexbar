# Generated by Django 5.0.7 on 2024-08-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_category_posts_alter_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='has_html',
            field=models.BooleanField(default=False, verbose_name='Has HTML'),
        ),
    ]
