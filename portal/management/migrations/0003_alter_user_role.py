# Generated by Django 4.1.3 on 2023-02-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_user_middle_name_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.TextField(default='Ученик', max_length=15),
        ),
    ]