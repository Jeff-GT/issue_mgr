from django.urls import path
from accounts import views
from .views import SignUpView


urlpatterns = [
  path("logout/", views.LogOutView.as_view(), name="logout_"),
  path("signup/", SignUpView.as_view(), name="signup"),
]