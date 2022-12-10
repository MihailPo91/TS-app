# Generated by Django 4.1.1 on 2022-12-01 20:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_tripshareuser_age_tripshareuser_landmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripshareuser',
            name='follows',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
