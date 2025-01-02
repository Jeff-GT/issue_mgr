from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import (
  CustomUserCreationForm,
  CustomUserChangeForm
)
  # Register your models here.
class CustomUserAdmin(UserAdmin):
  list_display = [
      "username", "email", "role", "is_staff"
  ]
  model = CustomUser
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  add_fieldsets = (
    (
      None, {
        "classes": ("wide", ),
        "fields": ("username", "email", "is_staff", "role", "password1", "password2"),
      }
  ),
  )
  fieldsets = UserAdmin.fieldsets + (
    (None, {"fields": ("role", )}),
  )

admin.site.register(CustomUser, CustomUserAdmin)