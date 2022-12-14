# Generated by Django 4.1.1 on 2022-12-03 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landmarks', '0005_rename_photo_landmark_main_photo'),
        ('photos', '0010_photo_landmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='landmark',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.RESTRICT, to='landmarks.landmark'),
        ),
    ]
