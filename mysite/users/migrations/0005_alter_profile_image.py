# Generated by Django 5.0.4 on 2024-06-10 10:26

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(upload_to=users.models.user_directory_path),
        ),
    ]
