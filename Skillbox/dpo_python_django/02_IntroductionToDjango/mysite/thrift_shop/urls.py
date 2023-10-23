from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("skyrim/", views.skyrim),
    path("doom/", views.doom),
    path("fallout/", views.fallout),
    path("prey/", views.prey),
    path("quake/", views.quake),
]
