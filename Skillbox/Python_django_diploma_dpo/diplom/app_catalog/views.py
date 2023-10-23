from rest_framework import authentication, permissions, viewsets, status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app_products.models import Product
from app_products.serializers import ProductSerializer
from .pagination import CatalogResultsSetPagination


class CatalogWithOut(ListAPIView, GenericAPIView):
    """
    View to product in the system.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CatalogResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    def get(self, request, **kwargs):
        return self.list(request)
