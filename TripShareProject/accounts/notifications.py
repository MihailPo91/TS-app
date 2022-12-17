from django.contrib.auth import get_user_model


from TripShareProject.common.models import Notification


UserModel = get_user_model()


def create_notification_for_new_follow_on_user(user, follower):
    to = user
    link = f'http://127.0.0.1:8000/accounts/profile/{follower.pk}/'
    message = f'{follower.username} just followed you! You now have {user.followed_by.count()} followers!'
    notification = Notification.objects.create(message=message)
    notification.receiver.add(to)
    notification.link = link
    notification.save()
