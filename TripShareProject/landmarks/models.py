from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse

from TripShareProject.accounts.validators import contains_only_letters_and_whitespace_validator


class Landmark(models.Model):

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        validators=[contains_only_letters_and_whitespace_validator, ]
    )
    main_photo = CloudinaryField(
        'image',
        null=False,
        blank=False,
        # Scaling for performance with cloudinary
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
        validators=[MinLengthValidator(100), MaxLengthValidator(10000)]
    )

    date_time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('landmark details', args=[self.pk])
