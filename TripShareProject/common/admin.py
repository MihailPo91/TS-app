from django.contrib import admin

from TripShareProject.common.models import Comment, Rating, Like


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('to_photo', 'user', )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('landmark', 'user', 'rating', )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    readonly_fields = ('to_photo', 'user', )
