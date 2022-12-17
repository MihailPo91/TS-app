from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from TripShareProject.common.models import Rating
from TripShareProject.landmarks.forms import LandmarkCreateForm, LandmarkEditForm, SearchForm
from TripShareProject.landmarks.models import Landmark
from TripShareProject.landmarks.notifications import create_notification_for_every_user_on_landmark_creation

UserModel = get_user_model()


class LandmarksHomeFeed(LoginRequiredMixin, views.ListView):
    model = Landmark
    template_name = 'landmark/landmark-home-feed.html'
    context_object_name = 'landmark_list'
    paginate_by = 10
    form_class = SearchForm

    def get_queryset(self):
        # queryset here is used to order landmarks and for the search form
        queryset = super().get_queryset().order_by('date_time_added')
        form = self.form_class(self.request.GET)
        if form.is_valid():
            # we pass info here from the user via the query
            return Landmark.objects.filter(name__icontains=form.cleaned_data['query'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        # context to add the search form
        context = super().get_context_data(**kwargs)
        form = SearchForm()
        context['search_form'] = form
        return context


class LandmarkDetailsView(LoginRequiredMixin, views.DetailView):
    model = Landmark
    template_name = 'landmark/landmark-details.html'
    context_object_name = 'landmark'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO Fix this first try / except since it's obsolete
        try:
            your_rating = Rating.objects.filter(user=self.request.user, landmark=self.object.id).last().rating or None
        except AttributeError:
            your_rating = None
        ratings = Rating.objects.filter(landmark=self.object.id)
        # we actually need this here for when we add new landmark and there is no rating yet
        # even the default didn't fix it and gave me ZeroDivisionError, so it has to be handled
        # TODO find a way to make the default value to work
        try:
            average_rating = (sum([r.rating for r in ratings]) / ratings.count())
        except ZeroDivisionError:
            average_rating = None
            # if we pass none to the context it's handled by the template
        context['average_rating'] = average_rating
        context['all_ratings'] = self.object.rating_set.all()
        if your_rating:
            context['your_rating'] = your_rating

        return context


class LandmarkAddView(PermissionRequiredMixin, views.CreateView):
    model = Landmark
    form_class = LandmarkCreateForm
    template_name = 'landmark/landmark-add.html'
    success_url = reverse_lazy('landmark home')

    permission_required = 'landmarks.add_landmark',
    permission_denied_message = "Sorry, you don't have permission to add landmarks"

    def form_valid(self, form):
        if form.is_valid():
            landmark = form.save(commit=False)
            landmark.save()
            # this actually feels ok since landmark creations are made only by staff and cannot be spammed
            create_notification_for_every_user_on_landmark_creation(landmark)
            return redirect('landmark home')


class LandmarkEditView(PermissionRequiredMixin, views.UpdateView):
    model = Landmark
    form_class = LandmarkEditForm
    template_name = 'landmark/landmark-edit.html'
    success_url = reverse_lazy('landmark home')

    permission_required = 'landmarks.change_landmark',
    permission_denied_message = "Sorry, you don't have permission to add landmarks"


