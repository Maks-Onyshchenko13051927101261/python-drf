from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from apps.books.filter import filter_books

from .models import BookModel
from .serializers import BookSerializer


# Готовий клас DRF для отримання списку книг і створення нових
class BookListCreateView(ListCreateAPIView):
    # Вказуємо серіалізатор для роботи з даними книги
    serializer_class = BookSerializer

    # Визначаємо, які книги потрібно отримати з бази даних
    def get_queryset(self):
        # Передаємо параметри запиту у функцію фільтрації
        return filter_books(self.request.query_params)


# Готовий клас DRF для отримання, оновлення та видалення книги
class BookDetailView(RetrieveUpdateDestroyAPIView):
    # Вказуємо серіалізатор для роботи з даними книги
    serializer_class = BookSerializer

    # Вказуємо набір книг, серед яких DRF шукатиме потрібну за ID
    queryset = BookModel.objects.all()
