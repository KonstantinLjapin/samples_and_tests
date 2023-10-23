from .models import Product, Review, Picture
from rest_framework import serializers


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        Depth = 3
        model = Picture
        fields = ['images']


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        Depth = 1
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    images = ImagesSerializer(instance='images', many=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = str(data['category'])
        data['images'] = [str(images.images.url) for images in instance.images.all()]

        return data

    class Meta:
        Depth = 3
        model = Product
        fields = '__all__'


"""("id", "category", "price", "count", "date",
                  "title", "description", "fullDescription", "href", "freeDelivery",
                  "images", "reviews", "specifications", "rating")"""
