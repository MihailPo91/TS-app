from django.contrib.auth import views as auth_views
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
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='passwords/change-password.html',
            success_url='/'
        ),
        name='change_password'
    ),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='passwords/password_reset.html',
             subject_template_name='passwords/password_reset_subject.txt',
             email_template_name='passwords/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='passwords/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='passwords/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='passwords/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
