from django.urls import path

from TripShareProject.common.views import ShowHomepageAsGuest, add_comment, like_view, follow_view, \
    tag_user_to_landmark, about_page_view, add_rating

urlpatterns = [
    path('', ShowHomepageAsGuest.as_view(), name='home'),
    path('comment/<int:photo_id>/', add_comment, name='add comment'),
    path('like/<int:photo_id>/', like_view, name='like'),
    path('follow/<int:pk>/', follow_view, name='follow'),
    path('tag/<int:pk>/', tag_user_to_landmark, name='tag'),
    path('rate/<int:pk>/', add_rating, name='add rating'),
    path('about/', about_page_view, name='about')
]
