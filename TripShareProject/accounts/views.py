from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.decorators.cache import cache_page

from TripShareProject import settings
from TripShareProject.accounts.forms import RegisterForm, LoginForm, TripUserEditForm
from TripShareProject.common.models import Notification
from TripShareProject.photos.models import Photo

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    model = UserModel
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        email = form.cleaned_data['email']
        self.set_group()
        self.email(email)
        login(self.request, self.object)
        return result

    def set_group(self):
        user = self.object
        group = Group.objects.get(name='member')
        user.groups.add(group)
        user.save()

    @staticmethod
    def email(email):
        subject = 'Welcome to TripShare'
        message = 'TripShare is welcoming you as our newest member. We wish you happy sharing and awesome time with our application! Enjoy your stay and remember - Only the shared trip is a finished trip!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)


class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('photo home')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class ShowProfileDetailsView(LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'accounts/profile_details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes = sum([photo.like_set.count() for photo in self.object.owned_by.all()])
        context['total_likes'] = total_likes
        visited = [landmark for landmark in self.object.visits.all()]
        all_posted_photos = Photo.objects.filter(owner__exact=self.object.id)
        context['all_photos'] = all_posted_photos
        context['visited'] = visited

        return context


class UserEditView(LoginRequiredMixin, views.UpdateView):
    model = UserModel
    form_class = TripUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_queryset(self):

        queryset = super(UserEditView, self).get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    model = UserModel
    success_url = reverse_lazy('home')
    template_name = 'accounts/profile-delete.html'

    def get_queryset(self):
        queryset = super(UserDeleteView, self).get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset


@cache_page(60 * 30)
@login_required
def show_user_photo_gallery(request, pk):
    user = UserModel.objects.get(pk=pk)
    if request.user.pk != user.pk and request.user not in user.followed_by.all():
        raise PermissionDenied('Please do not try that!')
    try:
        user_photos = Photo.objects.filter(owner=user)
    except AttributeError:
        user_photos = None
    context = {
        'user': user,
        'user_photos': user_photos
    }

    return render(request, 'photos/../../templates/accounts/photo_gallery.html', context=context)


@login_required
def show_user_followers_list(request, pk):
    user = UserModel.objects.get(pk=pk)
    if request.user.pk != user.pk and request.user not in user.followed_by.all():
        raise PermissionDenied('Please do not try that!')
    followers = user.followed_by.all()
    context = {'followers': followers, 'user': user}

    return render(request, 'accounts/followers-list.html', context=context)


@login_required
def show_user_followed_users(request, pk):
    user = UserModel.objects.get(pk=pk)
    if request.user.pk != user.pk and user not in request.user.follows.all():
        raise PermissionDenied('Please do not try that!')
    user_follows = user.follows.all()
    context = {'follows': user_follows, 'user': user}

    return render(request, 'accounts/follows-users-list.html', context=context)


@login_required
def show_user_notifications(request, pk):
    user = UserModel.objects.get(pk=pk)
    if request.user.pk != user.pk:
        raise PermissionDenied('Please do not try that!')
    notifications = Notification.objects.filter(receiver=user).order_by('-date_time_created')

    context = {'notifications': notifications}

    return render(request, 'accounts/notifications/notification-list.html', context=context)
