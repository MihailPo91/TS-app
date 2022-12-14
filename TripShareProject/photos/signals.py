# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from TripShareProject.accounts.models import TripShareUser
# from TripShareProject.common.models import Notification
# from TripShareProject.photos.models import Photo


# @receiver(post_save, sender=Photo)
# def send_photo_create_notification(sender, instance, created, **kwargs):
#     if instance:
#         sender_user = instance.owner
#         to = sender_user.followed_by.all().first()
#         message = f'{sender_user.username} just posted a new photo. Go check it out!'
#         Notification.objects.create(receiver=to, message=message)
#         # notification.save()

