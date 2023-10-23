
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from app_catalog.views import CatalogWithOut
from app_products.views import DetailProducts
router = routers.DefaultRouter()

urlpatterns = [
    path('<int:pk>', DetailProducts.as_view()),
    path('popular', csrf_exempt(CatalogWithOut.as_view())),
    path('limited', csrf_exempt(CatalogWithOut.as_view())),
]
