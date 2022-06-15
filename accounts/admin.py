from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Language, Role

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username", "email", "first_name","last_name","role", "preferred_language", "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ('role', 'preferred_language')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ('role', 'preferred_language')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Role)
admin.site.register(Language)
