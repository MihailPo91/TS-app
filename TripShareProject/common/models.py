from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
from django.db import models

from TripShareProject.landmarks.models import Landmark
from TripShareProject.photos.models import Photo
from TripShareProject.accounts.models import TripShareUser

UserModel = get_user_model()

# Create your models here.


class Comment(models.Model):
    text = models.TextField(
        null=False,
        blank=False,
        default='',
        validators=[MaxLengthValidator(255, message='The maximum comment characters is 255')]
    )
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, default=1)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'From *{self.user}* to photo-id: {self.to_photo} --- {self.text}'


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'From {self.user} to {self.to_photo}'


class Rating(models.Model):

    RATING_CHOICES = [(1, '1'),
                      (2, '2'),
                      (3, '3'),
                      (4, '4'),
                      (5, '5'),
                      (6, '6'),
                      (7, '7'),
                      (8, '8'),
                      (9, '9'),
                      (10, '10')]
    MIN_POSSIBLE_RATING = 1
    MAX_POSSIBLE_RATING = 10

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(MIN_POSSIBLE_RATING), MaxValueValidator(MAX_POSSIBLE_RATING)]
    )
    comment = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'From {self.user} to {self.landmark} --- {self.rating}'


class Notification(models.Model):
    # sender = models.ForeignKey(
    #     UserModel,
    #     on_delete= models.CASCADE,
    #     null=True,
    #     blank=True,
    #     related_name='sent_from'
    # )
    receiver = models.ManyToManyField(
        UserModel,
        related_name='sent_to'
    )
    message = models.CharField(max_length=255)
    link = models.URLField(
        null=True,
        blank=True,
    )
    date_time_created = models.DateTimeField(auto_now_add=True)
