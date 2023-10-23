from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bill
from django.contrib.auth.decorators import login_required
from .forms import BillForm


class Login(LoginView):
    template_name = 'users/login.html'


class LogOut(LogoutView):
    template_name = 'users/logout.html'


class UsersList (ListView):
    model = User
    template_name = 'users/users.html'


class RegView(CreateView):
    template_name = 'users/reg.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class BillList (ListView):
    model = Bill
    template_name = 'users/product.html'


class RegBillView(CreateView):
    template_name = 'users/buy_product.html'
    fields = '__all__'
    model = Bill
    success_url = reverse_lazy('main')
