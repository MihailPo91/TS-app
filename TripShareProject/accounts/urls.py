from django.urls import path, include

from TripShareProject.accounts.views import RegisterUserView, ShowProfileDetailsView, MyLogoutView, MyLoginView, \
    UserEditView, show_user_photo_gallery, UserDeleteView, show_user_followers_list, show_user_followed_users

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/<int:pk>/', include([
        path('', ShowProfileDetailsView.as_view(), name='profile details'),
        path('edit/', UserEditView.as_view(), name='profile edit'),
        path('gallery/', show_user_photo_gallery, name='profile gallery'),
        path('delete/', UserDeleteView.as_view(), name='profile delete'),
        path('followers/', show_user_followers_list, name='show followers'),
        path('follows/', show_user_followed_users, name='show following')
    ])),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
