from django.contrib.auth.views import LoginView, TemplateView, LogoutView
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Document
from .forms import PostForm


class Login(LoginView):
    template_name = 'app_load/login.html'


class LogOut(LogoutView):
    template_name = 'app_load/logout.html'


class Load(PermissionRequiredMixin, TemplateView):
    template_name = 'app_load/load.html'
    permission_required = 'app_load.change_post'
    model = Document
    form_class = PostForm
    success_url = reverse_lazy('home')
