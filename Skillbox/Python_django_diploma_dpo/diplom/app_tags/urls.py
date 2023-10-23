from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from .views import TagWithOut
router = routers.DefaultRouter()


urlpatterns = [
    path('', csrf_exempt(TagWithOut.as_view())),
]
