# Generated by Django 4.1.1 on 2022-12-07 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]