# Generated by Django 4.1.1 on 2022-12-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_delete_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
