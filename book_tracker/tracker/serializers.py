from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        exclude = ('user', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'first_name', 'first_name', 'token',)
