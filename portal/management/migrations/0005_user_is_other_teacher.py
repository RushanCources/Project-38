# Generated by Django 4.2.3 on 2023-08-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0004_user_full_name_alter_user_middle_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_other_teacher",
            field=models.BooleanField(default=False),
        ),
    ]
