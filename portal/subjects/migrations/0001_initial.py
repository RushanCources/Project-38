# Generated by Django 4.1.3 on 2023-05-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=30)),
                ('Type', models.CharField(max_length=10)),
                ('Subject', models.CharField(max_length=20)),
                ('Status', models.CharField(max_length=20)),
                ('Descript', models.CharField(max_length=2000)),
                ('Class_of_subject', models.CharField(max_length=100)),
                ('Class_of_tag', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
