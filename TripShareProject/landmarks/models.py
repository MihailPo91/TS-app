from cloudinary.models import CloudinaryField
from django.db import models
from django.urls import reverse


class Landmark(models.Model):

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    main_photo = CloudinaryField(
        'image',
        null=False,
        blank=False,
        transformation=[
            {'width': 1600, 'crop': "scale"},
            {'fetch_format': "auto"}
        ]
    )
    location = models.URLField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    date_time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('landmark details', args=[self.pk])
