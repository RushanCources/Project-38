# Generated by Django 4.1.7 on 2023-05-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image_url',
            field=models.FilePathField(null=True, path='static/img/announcements/covers'),
        ),
    ]
