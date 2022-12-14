from django.contrib.auth import get_user_model

from TripShareProject.common.models import Notification
from TripShareProject.photos.models import Photo

UserModel = get_user_model()


def create_notification_for_like_on_user_photo(like):
    photo = Photo.objects.filter(id=like.to_photo_id).first()
    to = photo.owner
    link = f'http://127.0.0.1:8000/photos/{photo.pk}/'
    message = f'{like.user.username} just liked your photo! The photo now has {photo.like_set.count()} likes!'
    notification = Notification.objects.create(message=message)
    notification.receiver.add(to)
    notification.link = link
    notification.save()


def create_notification_for_comment_on_user_photo(comment):
    photo = Photo.objects.filter(id=comment.to_photo_id).first()
    to = photo.owner

    if comment.user == to:
        return None

    link = f'http://127.0.0.1:8000/photos/{photo.pk}/#comments'
    message = f'{comment.user.username} just commented your photo! -- {comment.user.username}: {comment.text}'
    notification = Notification.objects.create(message=message)
    notification.receiver.add(to)
    notification.link = link
    notification.save()
