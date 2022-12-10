# Generated by Django 4.1.1 on 2022-12-02 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landmarks', '0005_rename_photo_landmark_main_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0004_alter_comment_to_photo_alter_comment_user_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landmark', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='landmarks.landmark')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
