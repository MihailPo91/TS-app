# Generated by Django 4.1.1 on 2022-12-15 21:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0022_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default='', validators=[django.core.validators.MaxLengthValidator(2555, message='The maximum comment characters is 255')]),
        ),
    ]
