from django.urls import path, include

from TripShareProject.landmarks.views import LandmarksHomeFeed, LandmarkDetailsView, LandmarkAddView, LandmarkEditView

urlpatterns = [
    path('', LandmarksHomeFeed.as_view(), name='landmark home'),
    path('add/', LandmarkAddView.as_view(), name='landmark add'),
    path('<int:pk>/', include([
        path('', LandmarkDetailsView.as_view(), name='landmark details'),
        path('edit/', LandmarkEditView.as_view(), name='landmark edit'),
        # path('delete/', LandmarkDeleteView.as_view(), name='landmark add')
    ]))
]
