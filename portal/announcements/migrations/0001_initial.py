# Generated by Django 4.1.4 on 2023-02-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('is_pinned', models.BooleanField(default=False)),
                ('date_of_expiring', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]