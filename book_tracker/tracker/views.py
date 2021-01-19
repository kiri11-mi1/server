from rest_framework.response import Response
from rest_framework import viewsets

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from . import models
from .service.utils import get_token
from . import serializers


class UserView(viewsets.ViewSet):
    def registration(self, request):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        if not email:
            return Response({'error': 'email is empty'}, status=500)

        if not first_name:
            return Response({'error': 'first_name is empty'}, status=500)

        if not last_name:
            return Response({'error': 'last_name is empty'}, status=500)

        if not password:
            return Response({'error': 'password is empty'}, status=500)

        try:
            validate_email(email)
        except ValidationError:
            return Response({'error': 'bad email'}, status=500)
        
        user = models.User.objects.filter(email=email).first()
        if user:
            return Response({'error': 'email is already exist'}, status = 500)
        
        user = models.User(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.token = get_token()
        user.set_password_hash(password)
        user.save()

        return Response({'token': user.token}, status=200)


    def login(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not password:
            return Response({'error': 'password is already exist'}, status=500)
        
        if not email:
            return Response({'error': 'email is empty'}, status=500)
        
        user = models.User.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'bad email'}, status = 500)

        if not user.check_password(password):
            return Response({'error': 'bad password'}, status = 500)
        
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)


class BookView(viewsets.ViewSet):
    pass
