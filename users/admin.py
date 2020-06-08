from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'mobile_number','is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('mobile_number', 'birth_date')}),
    )  # this will allow to change these fields in admin module
