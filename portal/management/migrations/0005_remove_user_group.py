# Generated by Django 4.1.7 on 2023-03-18 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_user_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='group',
        ),
    ]