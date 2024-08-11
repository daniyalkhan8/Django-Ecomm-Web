from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "first_name", "is_staff", "is_active",]
    list_filter = ["email", "first_name", "is_staff", "is_active",]

    fieldsets = [
        [None, {"fields": ["first_name", "last_name", "email", "dob", "profile_picture"]}],
        ["Address Information", {"fields": ["city", "street", "state", "postal_code"]}],
        ["Permissions", {"fields": ["is_staff", "is_active", "groups", "user_permissions"]}]
    ]

    add_fieldsets = [
        [
            None, {
                "classes": ("wide", ),
                "fields": (
                    "first_name", 
                    "last_name", 
                    "email", 
                    "password1", 
                    "password2", 
                    "is_staff", 
                    "is_active", 
                    "groups", 
                    "user_permissions"
                )
            }
        ]
    ]

    search_fields = ("email", "first_name")
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
