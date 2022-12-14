from TripShareProject.common.models import Notification


def has_unread_notifications(user):
    notifications = Notification.objects.filter(receiver=user)
    unread = [n for n in notifications if not n.is_read]
    if unread:
        return len(unread)
    else:
        return None
