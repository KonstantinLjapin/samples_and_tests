from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    fullName = serializers.SerializerMethodField('get_user_full_name')

    def get_user_full_name(self, obj):
        request = self.context['request']
        user = request.user
        name = user.first_name + " " + user.last_name
        return name

    class Meta:
        model = User
        fields = ['fullName', 'email', 'phone', 'avatar']
