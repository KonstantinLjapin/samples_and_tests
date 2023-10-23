from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from .views import CategoryWithOut
router = routers.DefaultRouter()


urlpatterns = [
    path('ho/', CategoryWithOut.as_view()),

]
