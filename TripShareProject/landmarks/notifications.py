from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy

from TripShareProject.common.models import Notification
UserModel = get_user_model()


def create_notification_for_every_user_on_landmark_creation(landmark):
    receivers = [user for user in UserModel.objects.all()]
    link = f'http://127.0.0.1:8000/landmarks/{landmark.pk}/'
    message = f'A new landmark has just been created - {landmark.name}. Have you visited yet?'
    for user in receivers:
        notification = Notification.objects.create(message=message)
        notification.receiver.add(user)
        notification.link = link
        notification.save()
