from django.db import models


class User(models.Model):
    email = models.EmailField(verbose_name='Email')
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилие', max_length=30)
    token = models.CharField(verbose_name='Фамилие', max_length=30)


    def __str__(self):
        return f'{self.name}\t{self.last_name}'


    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'


class Book(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    author_name = models.CharField(verbose_name='Автор', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name}\t{self.author_name}'


    class Meta:
        verbose_name = u'Книга'
        verbose_name_plural = u'Книги'
