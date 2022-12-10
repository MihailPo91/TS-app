# Generated by Django 4.1.1 on 2022-12-08 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0011_alter_photo_landmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='owned_by', to=settings.AUTH_USER_MODEL),
        ),
    ]