from django.contrib import admin
from django.contrib.auth import get_user_model


UserModel = get_user_model()


@admin.register(UserModel)
class TripShareUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'pk', 'is_superuser')
    ordering = ('id', )
    readonly_fields = ('last_login', 'date_joined', )
    fieldsets = (
        (None, {"fields": ()}),
        ("Personal info", {"fields": ("username", "email", "first_name", "last_name")}),
        (
            "Auth Details",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Additional info", {"fields": ("last_login", "date_joined")}),
    )
