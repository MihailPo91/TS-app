from django.urls import reverse, reverse_lazy

from TripShareProject.common.models import Notification


def create_notification_for_user_followers_on_photo_creation(photo):
    to = [user for user in photo.owner.followed_by.all()]
    link = f'http://127.0.0.1:8000/photos/{photo.pk}/'
    message = f'{photo.owner} just posted a new photo from {photo.location}. Go check it out!'
    notification = Notification.objects.create(message=message)
    notification.receiver.add(*to)
    notification.link = link
    notification.save()
