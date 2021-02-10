from rest_framework.response import Response
from rest_framework import viewsets

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from . import models
from .service.utils import get_token
from . import serializers, docs

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


class UserView(viewsets.ViewSet):
    def registration(self, request):
        """Регистрация пользователя"""
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

        return Response({'token': user.token}, status=201)


    def login(self, request):
        """Вход в аккаунт"""
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
        return Response({'user': serializer.data}, status=200)


    def update(self, request):
        """Изменения информации о пользователе"""
        token = request.POST.get('token')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        if not token:
            return Response({'error': 'token is empty'}, status=500)

        try:
            user = models.User.objects.get(token=token)
        except:
            return Response({'error': 'not found user'}, status=404)

        if first_name:
            user.first_name = first_name

        if last_name:
            user.last_name = last_name

        if password:
            user.set_password_hash(password)

        user.save()
        serializer = serializers.UserSerializer(user)
        return Response({'user': serializer.data}, status=200)


    def delete(self, request):
        """Удаление пользователя"""
        token = request.POST.get('token')

        if not token:
            return Response({'error': 'token is empty'}, status=500)

        try:
            user = models.User.objects.get(token=token)
        except:
            return Response({'error': 'not found user'}, status=404)

        user.delete()
        return Response({"success": f'User {user.first_name} was deleted'}, status=200)


class BookView(viewsets.ViewSet):
    @swagger_auto_schema(**docs.swagger_get_book)
    @api_view(['GET'])
    def get(self, request):
        """Получение всех книг пользвателя"""
        token = request.POST.get('token')

        if not token:
            return Response({'error': 'token is empty'}, status=500)

        try:
            user = models.User.objects.get(token=token)
        except:
            return Response({'error': 'user not found'}, status=404)

        books = models.Book.objects.filter(user_id=user.id)
        serializer = serializers.BookSerializer(books, many=True)
        return Response({'books': serializer.data}, status=200)


    @swagger_auto_schema(**docs.swagger_add_book)
    @api_view(['POST'])
    def add(self, request):
        """Добавление книги в личную библиотеку"""
        token = request.POST.get('token')
        name = request.POST.get('name')
        author_name = request.POST.get('author_name')
        status = request.POST.get('status')

        if not name:
            return Response({'error': 'name is empty'}, status=500)

        if not author_name:
            return Response({'error': 'author_name is empty'}, status=500)
        
        if not token:
            return Response({'error': 'token is empty'}, status=500)

        if not status:
            return Response({'error': 'status is empty'}, status=500)

        try:
            user = models.User.objects.get(token=token)
        except:
            return Response({'error': 'user not found'}, status=404)
        
        book = models.Book(
            name=name,
            author_name=author_name,
            status=status,
            user=user
        )

        book.save()
        serializer = serializers.BookSerializer(book)
        return Response({'book': serializer.data}, status=201)


    @swagger_auto_schema(**docs.swagger_update_book)
    @api_view(['PUT'])
    def update(self, request):
        """Обновление ифнормации о кинге"""
        token = request.POST.get('token')
        id = request.POST.get('id')
        name = request.POST.get('name')
        author_name = request.POST.get('author_name')
        status = request.POST.get('status')

        if not token:
            return Response({'error': 'token is empty'}, status=500)
        
        if not id:
            return Response({'error': 'id is empty'}, status=500)

        try:
            user = models.User.objects.get(token=token)
        except:
            return Response({'error': 'user not found'}, status=404)

        try:
            book = models.Book.objects.get(id=id)
        except:
            return Response({'error': 'not found book'}, status=404)

        if name:
            book.name = name
        
        if author_name:
            book.author_name = author_name

        if status:
            book.status = status

        book.save()
        serializer = serializers.BookSerializer(book)
        return Response({'book': serializer.data}, status=200)
    

    @swagger_auto_schema(**docs.swagger_delete_book)
    @api_view(['DELETE'])
    def delete(self, request):
        """Удаление книги из личной библиотеки"""
        token = request.POST.get('token')
        id = request.POST.get('id')

        if not token:
            return Response({'error': 'token is empty'}, status=500)

        if not id:
            return Response({'error': 'id is empty'}, status=500)

        try:
            user = models.User.objects.get(token=token)
        except:
            return Response({'error': 'user not found'}, status=404)
        
        try:
            book = models.Book.objects.get(id=id)
        except:
            return Response({'error': 'not found book'}, status=404)

        book.delete()

        return Response({"success": f"book '{book.name}' was deleted"}, status=200)

