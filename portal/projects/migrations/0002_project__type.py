# Generated by Django 4.2.1 on 2023-08-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
