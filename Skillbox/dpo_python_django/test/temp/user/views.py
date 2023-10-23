from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from django.contrib.auth.models import User, UserManager


class Login(LoginView):
    template_name = 'users/login.html'


class LogOut(LogoutView):
    template_name = 'users/logout.html'


class UserList(ListView):
    model = User
