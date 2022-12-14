from django.urls import path, include

from TripShareProject.common.views import ShowHomepageAsGuest, add_comment, like_view, follow_view, \
    tag_user_to_landmark, about_page_view, add_rating, copy_link_to_clipboard, delete_notification, show_contacts_view, \
    successful_message_sent

urlpatterns = [
    path('', ShowHomepageAsGuest.as_view(), name='home'),
    path('comment/<int:photo_id>/', add_comment, name='add comment'),
    path('like/<int:photo_id>/', like_view, name='like'),
    path('follow/<int:pk>/', follow_view, name='follow'),
    path('tag/<int:pk>/', tag_user_to_landmark, name='tag'),
    path('rate/<int:pk>/', add_rating, name='add rating'),
    path('share/<int:pk>/', copy_link_to_clipboard, name='share'),
    path('about/', about_page_view, name='about'),
    path('notification/<int:pk>/delete/', delete_notification, name='delete notification'),
    path('contact/', show_contacts_view, name='contact'),
    path('message-sent/', successful_message_sent, name='success sent')
]
