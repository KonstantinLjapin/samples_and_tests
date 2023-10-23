from django.shortcuts import render
from django.views.generic import ListView
from .models import Bill


class ClassBasedView(ListView):
    template_name = "bill.html"
    model = Bill
