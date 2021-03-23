from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class LoggedInView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/loggedin.html"