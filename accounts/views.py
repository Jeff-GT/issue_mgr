from django.views.generic import TemplateView, CreateView
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy

class LogOutView(TemplateView):
  template_name = "registration/logout_.html"

  def get(self, request):
    return self.render_to_response(self.get_context_data())

  def post(self, request):
    logout(request)
    return redirect('list')

class SignUpView(CreateView):
  template_name = "registration/signup.html"
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
