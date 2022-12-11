from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from TripShareProject.common.models import Rating
from TripShareProject.landmarks.forms import LandmarkCreateForm, LandmarkEditForm, SearchForm
from TripShareProject.landmarks.models import Landmark

UserModel = get_user_model()


class LandmarksHomeFeed(LoginRequiredMixin, views.ListView):
    model = Landmark
    template_name = 'landmark/landmark-home-feed.html'
    context_object_name = 'landmark_list'
    paginate_by = 5
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset().order_by('date_time_added')
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Landmark.objects.filter(name__icontains=form.cleaned_data['query'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
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
        try:
            your_rating = Rating.objects.filter(user=self.request.user, landmark=self.object.id).last().rating or None
        except AttributeError:
            your_rating = None
        ratings = Rating.objects.filter(landmark=self.object.id)
        try:
            average_rating = (sum([r.rating for r in ratings]) / ratings.count())
        except ZeroDivisionError:
            average_rating = None
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


class LandmarkEditView(PermissionRequiredMixin, views.UpdateView):
    model = Landmark
    form_class = LandmarkEditForm
    template_name = 'landmark/landmark-edit.html'
    success_url = reverse_lazy('landmark home')

    permission_required = 'landmarks.change_landmark',
    permission_denied_message = "Sorry, you don't have permission to add landmarks"


