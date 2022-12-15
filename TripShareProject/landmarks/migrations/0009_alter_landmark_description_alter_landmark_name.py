# Generated by Django 4.1.1 on 2022-12-15 21:57

import TripShareProject.accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmarks', '0008_alter_landmark_main_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='description',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(100), django.core.validators.MaxLengthValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='name',
            field=models.CharField(max_length=50, validators=[TripShareProject.accounts.validators.contains_only_letters_validator]),
        ),
    ]