from django.contrib import admin

from TripShareProject.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('photo', 'owner', )
