from rest_framework import serializers
from .models import Tag


class TagWithOutModelSerializer(serializers.Serializer):

    class Meta:
        Depth = 1
        queryset = Tag.objects.all()
        fields = '__all__'
