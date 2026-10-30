from rest_framework import serializers

from .models import BookModel


# Серіалізатор для перетворення та перевірки даних книги
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # Вказуємо модель, з якою працює серіалізатор
        model = BookModel

        # Перелічуємо поля, які використовуватиме API
        fields = (
            "id",
            "title",
            "author",
            "published_date",
            "isbn",
            "pages",
            "language",
            "created_at",
            "updated_at",
        )
