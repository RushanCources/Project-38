# Generated by Django 4.2 on 2023-04-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_remove_user_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.IntegerField(null=True),
        ),
    ]
