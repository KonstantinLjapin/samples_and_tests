from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClassBasedView.as_view(), name='bill'),
]
