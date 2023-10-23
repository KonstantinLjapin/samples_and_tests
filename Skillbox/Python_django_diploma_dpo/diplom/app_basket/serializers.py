from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        Depth = 1
        model = Cart
        fields = '__all__'
