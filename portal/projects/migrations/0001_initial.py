# Generated by Django 4.1.7 on 2023-03-11 13:25
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('_status', models.CharField(max_length=30)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.student')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.teacher')),
            ],
        ),
    ]
