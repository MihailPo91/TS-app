import random

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404

from TripShareProject.common.forms import CommentForm, RatingForm
from TripShareProject.common.models import Like, Rating
from TripShareProject.landmarks.models import Landmark
from TripShareProject.photos.models import Photo

UserModel = get_user_model()


# Create your views here.

class ShowHomepageAsGuest(views.View):

    @staticmethod
    def get(request):
        all_photos = Photo.objects.all().order_by('-date_time_of_publication')[:8]
        profile = request.user
        try:
            random_photo = random.choice(Photo.objects.all())
        except ObjectDoesNotExist:
            random_photo = None
        if profile.id:
            context = {
                'all_photos': all_photos,
                'profile': profile,
                'random_photo': random_photo
            }
        else:
            context = {
                'all_photos': all_photos,
            }

        return render(request, 'common/homepage.html', context=context)


@login_required
def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def like_view(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def follow_view(request, pk):
    user_to_follow = UserModel.objects.get(pk=pk)
    current_user = get_object_or_404(UserModel, username=request.user.username)
    following = current_user.follows.all()

    if user_to_follow != current_user:
        if user_to_follow in following:
            current_user.follows.remove(user_to_follow.id)
        else:
            current_user.follows.add(user_to_follow.id)

    return redirect('profile details', pk)


@login_required
def tag_user_to_landmark(request, pk):
    landmark = Landmark.objects.get(pk=pk)
    current_user = get_object_or_404(UserModel, username=request.user.username)
    try:
        is_visited = current_user.visits.get(pk=pk)
    except Exception:
        current_user.visits.add(landmark.id)

    else:
        current_user.visits.remove(landmark.id)

    return redirect(request.META['HTTP_REFERER'] + '#tag')


def about_page_view(request):
    return render(request, 'common/about.html')


@login_required
def add_rating(request, pk):
    landmark = Landmark.objects.get(pk=pk)
    already_rated = Rating.objects.filter(user=request.user, landmark=landmark).last()
    if request.method == 'POST':

        if already_rated:
            form = RatingForm(request.POST)
            Rating.objects.get(user=request.user, landmark=landmark).delete()
            if form.is_valid():
                rating = form.save(commit=False)
                rating.user = request.user
                rating.landmark = landmark
                rating.save()

                return redirect('landmark details', landmark.pk)
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.landmark = landmark
            rating.save()

            return redirect('landmark details', landmark.pk)
    else:
        if already_rated:
            form = RatingForm(initial=already_rated.__dict__)

        else:
            form = RatingForm()

        context = {'form': form, 'is_rated_already': already_rated, 'landmark': landmark}
        return render(request, 'common/add-rating.html', context=context)
