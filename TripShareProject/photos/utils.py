from django.contrib.auth import get_user_model

from TripShareProject.photos.models import Photo

UserModel = get_user_model()


def get_followed_content(user_id):
    user = UserModel.objects.get(id=user_id)
    following = user.follows_set.all()
    all_photos = Photo.objects.filter(owner__in=following)
    return all_photos
