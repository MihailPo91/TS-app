# Generated by Django 4.1.1 on 2022-11-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_alter_photo_date_time_of_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, default='Bulgaria', max_length=30, null=True),
        ),
    ]
