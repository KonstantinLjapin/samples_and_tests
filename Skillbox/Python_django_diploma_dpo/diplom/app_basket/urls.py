from django.urls import include, path
from rest_framework import routers
from .views import CartWithOut
from django.views.decorators.csrf import csrf_exempt
router = routers.DefaultRouter()


urlpatterns = [
    path('', csrf_exempt(CartWithOut.as_view())),
]
