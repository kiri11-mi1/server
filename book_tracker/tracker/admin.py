from django.contrib import admin
from . import models

from random import randint as rd


class BookInline(admin.StackedInline):
    """Отзывы на странице фильма"""
    model = models.Book
    extra = 1
    readonly_fields = ("name", "author_name", "status")


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_email', 'get_token')
    list_display_links = ('first_name', 'last_name')
    readonly_fields = ('token', )
    inlines = [BookInline]


    def get_token(self, obj):
        return obj.token[:5] + '*'*rd(3, 10) + obj.token[-5:]
    

    def get_email(self, obj):
        return obj.email[:5] + '*'*rd(3, 10) + obj.email[-5:]


    get_token.short_description = 'Токен'
    get_email.short_description = 'Почта'


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'status')
    search_fields = ('name', 'author_name')
    list_filter = ('status',)


admin.site.site_title = "Book tracker"
admin.site.site_header = "Book tracker"
