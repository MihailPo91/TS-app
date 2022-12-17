from django.urls import path, include

from TripShareProject.photos.views import PhotoDetailsView, photo_home_feed, PhotoEditView, \
    PhotoDeleteView, FollowedContentView, PhotoCreateView

urlpatterns = [
    path('', photo_home_feed, name='photo home'),
    path('followed_posts/', FollowedContentView.as_view(), name='followed feed'),
    path('add/', PhotoCreateView.as_view(), name='photo add'),
    path('<int:pk>/', include([
        path('', PhotoDetailsView.as_view(), name='photo details'),
        path('edit/', PhotoEditView.as_view(), name='photo edit'),
        path('delete/', PhotoDeleteView.as_view(), name='photo delete'),
    ])
         ),
]
