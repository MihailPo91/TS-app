from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from TripShareProject.landmarks.models import Landmark

UserModel = get_user_model()


class Photo(models.Model):
    photo = CloudinaryField(
        'image',
        null=False,
        blank=False,
    )
    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default='Bulgaria'
    )
    description = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='owned_by'
    )

    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE, default=1, blank=True, null=True)

    def __str__(self):
        return f'{self.pk} - {self.owner} '

    def get_absolute_url(self):
        return reverse('photo details', kwargs={'pk': self.pk})
