# Generated by Django 4.1.1 on 2022-12-07 10:59

import TripShareProject.accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_tripshareuser_landmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripshareuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(119)]),
        ),
        migrations.AlterField(
            model_name='tripshareuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), TripShareProject.accounts.validators.contains_only_letters_validator]),
        ),
        migrations.AlterField(
            model_name='tripshareuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), TripShareProject.accounts.validators.contains_only_letters_validator]),
        ),
    ]
