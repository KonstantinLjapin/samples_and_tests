from django.urls import path
from . import views

urlpatterns = [
    path('advertisement/', views.ClassBasedViewAdvertisement.as_view()),
    path('', views.ClassBasedView.as_view()),

]
