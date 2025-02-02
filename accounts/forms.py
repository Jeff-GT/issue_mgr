from django.contrib.auth.forms import (
  UserCreationForm,
  UserChangeForm
)
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
  class Meta(UserChangeForm):
    model = CustomUser
    fields = UserCreationForm.Meta.fields + ("email", "role", "groups")

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm):
    model = CustomUser
    fields = UserChangeForm.Meta.fields