from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from rest_framework import mixins
from .models import Product
from .serializers import ProductSerializer
from .pagination import ProductResultsSetPagination
from rest_framework.views import APIView


class DetailProducts(generics.RetrieveAPIView):
    """
    View to product in the system.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]


