from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from .views import CatalogWithOut
from app_products.views import DetailProducts
router = routers.DefaultRouter()


urlpatterns = [
    path('', csrf_exempt(CatalogWithOut.as_view())),
    path('<int:pk>', DetailProducts.as_view()),
]
