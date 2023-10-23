from rest_framework import serializers
from app_products.serializers import ProductSerializer
from app_products.models import Product


class CatalogWithOutModelSerializer(serializers.Serializer):
    items = ProductSerializer(many=True, read_only=False)

    class Meta:
        Depth = 1
        queryset = Product.objects.all()
        fields = '__all__'
