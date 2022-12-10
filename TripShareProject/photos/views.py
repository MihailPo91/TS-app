from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page

from TripShareProject.common.forms import CommentForm
from TripShareProject.photos.forms import PhotoCreateForm, PhotoEditForm
from TripShareProject.photos.models import Photo


UserModel = get_user_model()


@login_required
def photo_home_feed(request):
    all_photos = Photo.objects.all().order_by('-date_time_of_publication')
    user = UserModel.objects.get(id=request.user.id)
    comment_form = CommentForm()

    try:
        all_liked_photos_by_request_user = [like.to_photo_id for like in user.like_set.all()]
    except AttributeError:
        all_liked_photos_by_request_user = []

    context = {
        'all_photos': all_photos,
        'all_liked_photos_by_request_user': all_liked_photos_by_request_user,
        'comment_form': comment_form,
    }

    return render(request, template_name='photos/photo-home-feed.html', context=context)


class FollowedContentView(LoginRequiredMixin, views.ListView):
    model = Photo
    template_name = 'accounts/followed_feed.html'
    context_object_name = 'photos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = CommentForm()
        user = UserModel.objects.get(id=self.request.user.id)
        try:
            all_liked_photos_by_request_user = [like.to_photo_id for like in user.like_set.all()]
        except AttributeError:
            all_liked_photos_by_request_user = []
        context['all_liked_photos_by_request_user'] = all_liked_photos_by_request_user
        context['comment_form'] = comment_form
        return context

    def get_queryset(self):
        user = UserModel.objects.get(id=self.request.user.id)
        followed = user.follows.all()
        queryset = Photo.objects.filter(owner__in=followed).order_by('-date_time_of_publication')
        return queryset


class PictureDetailsView(LoginRequiredMixin, views.DetailView):
    model = Photo
    template_name = 'photos/photo-details.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        comment_form = CommentForm()
        context = super().get_context_data(**kwargs)
        context['comment_form'] = comment_form
        context['likes'] = [like.user_id for like in self.object.like_set.all()]
        return context


class PictureEditView(LoginRequiredMixin, views.UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit.html'


class PictureDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Photo
    template_name = 'photos/photo-delete.html'
    success_url = reverse_lazy('photo home')


# @login_required
# def add_photo(request):
#     if request == 'POST':
#         form = PhotoCreateForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             photo = form.save(commit=False)
#             photo.owner = request.user
#             photo.save()
#             # form.save_m2m()
#             return redirect('photo home')
#     form = PhotoCreateForm()
#     context = {
#         'form': form
#     }
#     return render(request, template_name='photos/photo-create.html', context=context)

class PhotoCreateView(LoginRequiredMixin, views.CreateView):
    model = Photo
    template_name = 'photos/photo-create.html'
    success_url = reverse_lazy('photo home')
    form_class = PhotoCreateForm

    def form_valid(self, form):
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = self.request.user
            photo.save()
            return redirect('photo home')
