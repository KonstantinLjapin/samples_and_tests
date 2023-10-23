from django.shortcuts import render
from django.db import transaction
from django.urls import reverse_lazy
from .models import Product, Person
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
import logging


class Login(LoginView):
    template_name = 'users/login.html'

    def __call__(self, request):
        logger.info('Some log')


class LogOut(LogoutView):
    template_name = 'users/logout.html'

    def __call__(self, request):
        logger.info('Some log')


class UsersList(ListView):
    model = Person
    template_name = 'users/users.html'

    def __call__(self, request):
        logger.info('Some log')


class RegView(CreateView):
    template_name = 'users/reg.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def __call__(self, request):
        logger.info('Some log')


@transaction.atomic()
class ProductList(ListView):
    model = Product
    template_name = 'users/product.html'

    def __call__(self, request):
        logger.info('Some log')

    @transaction.atomic()
    def pub_list(self):
        with transaction.atomic():
            reduce_balace = self.wallet


class RegProductView(CreateView):
    template_name = 'users/buy_product.html'
    fields = '__all__'
    model = Product
    success_url = reverse_lazy('main')

    def __call__(self, request):
        logger.info('Some log')


logger = logging.getLogger(__name__)
