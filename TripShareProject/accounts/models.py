from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from TripShareProject.accounts.validators import contains_only_letters_validator
from TripShareProject.landmarks.models import Landmark


class TripShareUser(AbstractUser):
    MIN_NAME_LENGTH = 2
    MIN_AGE = 10
    MAX_AGE = 119

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=30,
        validators=(MinLengthValidator(MIN_NAME_LENGTH), contains_only_letters_validator,),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        validators=(MinLengthValidator(MIN_NAME_LENGTH), contains_only_letters_validator,),
        blank=True,
        null=True,
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(MIN_AGE), MaxValueValidator(MAX_AGE)],
        null=True,
        blank=True,
    )
    profile_picture = CloudinaryField(
        'image',
        null=True,
        blank=True,
        transformation=[
            {'width': 1200, 'crop': "scale"},
            {'fetch_format': "auto"}
        ]
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )
    follows = models.ManyToManyField(
        'TripShareUser',
        related_name='followed_by'
    )
    visits = models.ManyToManyField(
        Landmark,
        related_name='visited_by'
    )

    def get_user_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username



