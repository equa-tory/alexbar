# Generated by Django 5.0.7 on 2024-08-09 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name_ru',
        ),
    ]
