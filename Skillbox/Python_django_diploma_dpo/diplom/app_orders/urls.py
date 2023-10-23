from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from .views import OrderActive, Orders
router = routers.DefaultRouter()


urlpatterns = [
    path('', csrf_exempt(Orders.as_view())),
    path('active', csrf_exempt(OrderActive.as_view())),
]
