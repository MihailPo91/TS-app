# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from TripShareProject.common.models import Notification
# from .models import Photo
#
#
# @receiver(post_save, sender=Photo)
# def send_photo_create_notification(sender, instance, created, **kwargs):
#     if created:
#         to = instance.user.followed_by_set.all()
#         message = f'{instance.user.username} just posted a new photo from {instance.location}. Go check it out!'
#         notification = Notification.objects.create(message=message)
#         notification.receiver.add(*to)
#         notification.save()

