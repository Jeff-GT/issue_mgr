from django.views.generic import(
  CreateView,
  DetailView,
  UpdateView,
  DeleteView,
  ListView
)
from .models import Issue, Status
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

class IssueCreateView(CreateView):
  template_name = "issues/new.html"
  model = Issue
  fields = [
    "name", "summary", "description", "status", "assignee"
  ]

  def form_valid(self, form):
    form.instance.reporter = self.request.user
    return super().form_valid(form)



class IssueDetailView(DetailView):
  template_name = "issues/detail.html"
  model = Issue
  def test_func(self):
    issue = self.get_object()
    if issue.status.name != "":
      return True


class IssueUpdateView(UpdateView):
  template_name = "issues/edit.html"
  model = Issue
  fields = [
    "name", "summary", "status", 
  ]

  def test_func(self):
    issue = self.get_object()
    is_true = issue.reporter == self.request.user or issue.assignee == self.request.user
    return is_true

class IssueDeleteView(DeleteView):
  template_name = "issues/delete.html"
  model = Issue
  success_url = reverse_lazy("list")

class IssueListView(ListView):
  template_name = "issues/list.html"
  model = Issue
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context ["to_do"] = (
      Issue.objects
      .filter(status= Status.objects.get(name="to do"))
      .order_by("created_on").reverse
    )
    context ["in_progress"] = (
      Issue.objects
      .filter(status= Status.objects.get(name="in progress"))
      .order_by("created_on").reverse
    )
    context ["done"] = (
      Issue.objects
      .filter(status= Status.objects.get(name="done"))
      .order_by("created_on").reverse
    )
    return context