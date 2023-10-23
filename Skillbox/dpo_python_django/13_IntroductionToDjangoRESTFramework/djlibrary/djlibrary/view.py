from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from .models import Book
from .serializers import BookSerializer


class ListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()

    def get_queryset(self):
        queryset = Book.objects.all()
        item_name = self.request.query_params.get('title')
        if item_name:
            queryset = queryset.filter(name=item_name)
            return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)
