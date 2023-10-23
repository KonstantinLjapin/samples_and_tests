from django.shortcuts import render

from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Tag
from .serializers import TagWithOutModelSerializer


class TagWithOut(ListAPIView):
    """
    View to product in the system.
    """
    queryset = Tag.objects.all()
    serializer_class = TagWithOutModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset

    def get(self, request, **kwargs):
        return self.list(request)

