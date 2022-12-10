# Generated by Django 4.1.1 on 2022-11-06 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_initial'),
        ('photos', '0002_remove_photo_comments_photo_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='comments',
        ),
        migrations.AddField(
            model_name='photo',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='common.comment'),
        ),
    ]
