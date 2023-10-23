
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django import forms
from .models import *


class ClassBasedView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['just_title'] = 'Test1'
        context['just_text'] = 'Test2'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    @staticmethod
    def post(request, *args, **kwargs):
        return render(request, 'index.html')


class ClassBasedViewAdvertisement(TemplateView):
    template_name = "advertisements/advertisement_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['just_title'] = 'Test1'
        context['just_text'] = 'Test2'
        return context
