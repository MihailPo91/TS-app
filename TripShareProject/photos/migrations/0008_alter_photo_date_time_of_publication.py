# Generated by Django 4.1.1 on 2022-11-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_remove_photo_date_of_publication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_time_of_publication',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
