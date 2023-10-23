from django.shortcuts import redirect
from django.views.generic import ListView
from rest_framework import authentication, permissions, generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from app_products.models import Product
from app_products.serializers import ProductSerializer
from app_basket.models import Cart
from rest_framework.response import Response


class OrderActive(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        cart = Cart(request)
        data = list(cart.cart.values())
        return Response(data, status=HTTP_200_OK)

    def post(self, request):
        cart = Cart(request)
        product = get_object_or_404(Product, id=request.data['id'])
        cart.add(product=product)
        data = list(cart.cart.values())
        return Response(data, status=HTTP_200_OK)


class Orders(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    def get(self, request, **kwargs):
        return self.list(request)

    def post(self, request):
        cart = Cart(request)
        product = get_object_or_404(Product, id=request.data['id'])
        cart.add(product=product)
        data = list(cart.cart.values())
        return Response(data, status=HTTP_200_OK)