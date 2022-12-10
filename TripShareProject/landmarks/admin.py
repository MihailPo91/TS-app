from django.contrib import admin

from TripShareProject.landmarks.models import Landmark


@admin.register(Landmark)
class LandmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    ordering = ('name',)

