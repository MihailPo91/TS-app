# Generated by Django 4.1.1 on 2022-12-14 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0020_alter_notification_receiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_read',
        ),
    ]
