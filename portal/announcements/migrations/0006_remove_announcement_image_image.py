# Generated by Django 4.1.7 on 2023-03-12 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0005_remove_announcement_image_urls_announcement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='announcement_images')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='announcements.announcement')),
            ],
        ),
    ]