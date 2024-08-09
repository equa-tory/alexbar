# Generated by Django 5.0.7 on 2024-08-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_idea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL'),
        ),
    ]
