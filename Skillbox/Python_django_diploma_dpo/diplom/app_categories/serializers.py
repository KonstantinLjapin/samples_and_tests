from .models import Category, Subcategories
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        Depth = 1
        model = Category
        fields = '__all__'


class SubcategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        Depth = 1
        model = Subcategories
        fields = '__all__'
