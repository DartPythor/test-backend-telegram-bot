from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("telegram_id",)}),
        ("Права", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    list_display = ("telegram_id", "is_staff")
    ordering = ("telegram_id",)

admin.site.register(CustomUser, CustomUserAdmin)
