import random

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.mail import send_mail
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from pyperclip import copy

from TripShareProject import settings
from TripShareProject.accounts.notifications import create_notification_for_new_follow_on_user
from TripShareProject.common.forms import CommentForm, RatingForm, ContactForm
from TripShareProject.common.models import Like, Rating, Notification
from TripShareProject.common.notifications import create_notification_for_like_on_user_photo, \
    create_notification_for_comment_on_user_photo
from TripShareProject.landmarks.models import Landmark
from TripShareProject.photos.models import Photo

UserModel = get_user_model()


# Create your views here.

class ShowHomepageAsGuest(views.View):

    @staticmethod
    def get(request):
        all_photos = Photo.objects.all().order_by('-date_time_of_publication')[:8]
        profile = request.user
        # probably not necessary but if broke few times, so I prefer it handled
        try:
            random_photo = random.choice(Photo.objects.all())
        except ObjectDoesNotExist:
            random_photo = None
        # TODO Clean this later, it's obsolete
        if profile.id:
            context = {
                'all_photos': all_photos,
                'profile': profile,
                'random_photo': random_photo
            }
        else:
            context = {
                'all_photos': all_photos,
                'random_photo': random_photo
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
            create_notification_for_comment_on_user_photo(comment)

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
        # we create notification on every like, can be a bit spammy and can brake the site
        # TODO handle this notification with a signal and check for recent similar like to avoid overload
        create_notification_for_like_on_user_photo(like)

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def follow_view(request, pk):
    user_to_follow = UserModel.objects.get(pk=pk)
    current_user = get_object_or_404(UserModel, username=request.user.username)
    following = current_user.follows.all()

    # we cannot follow ourselves!
    if user_to_follow != current_user:
        if user_to_follow in following:
            current_user.follows.remove(user_to_follow.id)
        else:
            current_user.follows.add(user_to_follow.id)
            # TODO again this can make overload; put some kind of a timeout here
            create_notification_for_new_follow_on_user(user_to_follow, current_user)

    return redirect('profile details', pk)


@login_required
def tag_user_to_landmark(request, pk):
    landmark = Landmark.objects.get(pk=pk)
    current_user = get_object_or_404(UserModel, username=request.user.username)
    # try except is to keep template loading, it brakes otherwise
    try:
        is_visited = current_user.visits.get(pk=pk)
        if is_visited:
            current_user.visits.remove(landmark.id)
    except ObjectDoesNotExist:
        current_user.visits.add(landmark.id)

    return redirect(request.META['HTTP_REFERER'] + '#tag')


@login_required
def copy_link_to_clipboard(request, pk):
    photo = Photo.objects.get(pk=pk)
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', pk))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo.id}')


def about_page_view(request):
    return render(request, 'common/about.html')


@login_required
def add_rating(request, pk):
    landmark = Landmark.objects.get(pk=pk)
    already_rated = Rating.objects.filter(user=request.user, landmark=landmark).last()

    # we handle first posted rating and edit rating here 2 in 1, which is bad and has to be fixed
    # TODO separate this view into 2 views with 2 separate tasks
    if request.method == 'POST':

        # this is the edit part
        if already_rated:
            form = RatingForm(request.POST)
            Rating.objects.get(user=request.user, landmark=landmark).delete()
            if form.is_valid():
                rating = form.save(commit=False)
                rating.user = request.user
                rating.landmark = landmark
                rating.save()

                return redirect('landmark details', landmark.pk)

        # here is the creation part
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.landmark = landmark
            rating.save()

            return redirect('landmark details', landmark.pk)

    # that's for GET and my god its ugly
    # TODO I promise I will fix this ASAP
    else:
        if already_rated:
            form = RatingForm(initial=already_rated.__dict__)

        else:
            form = RatingForm()

        context = {'form': form, 'is_rated_already': already_rated, 'landmark': landmark}
        return render(request, 'common/add-rating.html', context=context)


@login_required
def delete_notification(request, pk):
    notification = Notification.objects.get(pk=pk)
    # security check here, we should not be deleting and reading other people's notifications
    if request.user not in notification.receiver.all():
        raise PermissionDenied('Please do not try that!')
    notification.delete()
    return redirect(request.META['HTTP_REFERER'])


def successful_message_sent(request):
    return render(request, 'contact/message_sent.html')


def show_contacts_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            # the contact form is anonymous therefore no email is needed from user
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['text']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_from, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('success sent')

    else:
        form = ContactForm()

        context = {'form': form}

        return render(request, 'contact/contact.html', context=context)
