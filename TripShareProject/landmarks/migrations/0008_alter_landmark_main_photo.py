# Generated by Django 4.1.1 on 2022-12-11 22:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landmarks', '0007_alter_landmark_date_time_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='main_photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]