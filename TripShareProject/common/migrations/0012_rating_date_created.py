# Generated by Django 4.1.1 on 2022-12-08 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_rating_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]