# Generated by Django 4.2.4 on 2023-08-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_rename_author_theme_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='subject',
        ),
        migrations.AddField(
            model_name='theme',
            name='subjects',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]
