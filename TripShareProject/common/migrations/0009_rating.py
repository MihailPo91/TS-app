# Generated by Django 4.1.1 on 2022-12-07 15:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landmarks', '0006_remove_landmark_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0008_alter_comment_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('landmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landmarks.landmark')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
