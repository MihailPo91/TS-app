from django.urls import re_path

from django.conf import settings

from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from TripShareProject.errors import error_404, error_500, error_403

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),
    path('accounts/', include('TripShareProject.accounts.urls')),
    path('', include('TripShareProject.common.urls')),
    path('landmarks/', include('TripShareProject.landmarks.urls')),
    path('photos/', include('TripShareProject.photos.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = error_403
handler404 = error_404
handler500 = error_500
