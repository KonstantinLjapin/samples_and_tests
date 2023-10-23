from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from .views import PaymentWithOut
router = routers.DefaultRouter()


urlpatterns = [
    path('', PaymentWithOut.as_view()),
]
