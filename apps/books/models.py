from django.db import models

from core.models import CoreConfig


# Модель книги, яка успадковує спільні поля та налаштування від CoreConfig
class BookModel(CoreConfig):
    # Назва книги
    title = models.CharField(max_length=200)

    # Автор книги
    author = models.CharField(max_length=100)

    # Дата публікації
    published_date = models.DateField()

    # ISBN книги, який має бути унікальним
    isbn = models.CharField(max_length=13, unique=True)

    # Кількість сторінок
    pages = models.IntegerField()

    # Мова книги
    language = models.CharField(max_length=30)

    # Повертає назву книги як її текстове представлення
    def __str__(self):
        return self.title
