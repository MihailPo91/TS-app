# Generated by Django 4.1.1 on 2022-12-15 21:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_remove_notification_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default='', validators=[django.core.validators.MaxLengthValidator(5)]),
        ),
    ]
