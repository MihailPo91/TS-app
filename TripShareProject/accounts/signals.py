# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from TripShareProject import settings
# from TripShareProject.accounts.models import TripShareUser
#
#
# @receiver(signal=post_save, sender=TripShareUser)
# def send_greeting_email(sender, instance, created, **kwargs):
#     if created:
#         subject = "Welcome to TripShare"
#         plain_message = f"Hello {sender.instance.user.username}! We are happy to see you joining TripShare community. Enjoy your stay and share many photos and happy memories"
#         to = instance.email
#         send_mail(subject=subject, message=plain_message, from_email=settings.EMAIL_HOST_USER, recipient_list=[to])
