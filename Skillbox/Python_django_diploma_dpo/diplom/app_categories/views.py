from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Subcategories
from .serializers import CategorySerializer, SubcategoriesSerializer


class CategoryWithOut(ListAPIView):
    """
    View to product in the system.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

    def get(self, request, **kwargs):
        return self.list(request)
