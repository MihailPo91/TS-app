# Generated by Django 4.1.1 on 2022-11-22 20:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landmarks', '0002_alter_landmark_visitors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landmark',
            name='visitors',
        ),
        migrations.AddField(
            model_name='landmark',
            name='visitors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
