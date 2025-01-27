from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'avatar', 'phone', 'country', 'password']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
