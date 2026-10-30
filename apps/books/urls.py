from django.urls import path

from .views import BookDetailView, BookListCreateView

# Маршрути API для роботи з книгами
urlpatterns = [
    # Отримання списку книг і створення нової книги
    path("", BookListCreateView.as_view(), name="book-list-create"),
    # Отримання, оновлення та видалення книги за її ID
    path("<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
