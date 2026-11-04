# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from apps.books.models import BookModel
# from apps.books.serializers import BookSerializer


# # APIView дозволяє вручну описати обробку HTTP-запитів.
# # На відміну від готових generic-класів, тут ми самостійно
# # отримуємо дані з ORM, викликаємо серіалізатор і формуємо відповідь.
# class BookListCreateView(APIView):
#     # GET /api/books/
#     # Отримує всі записи з таблиці книг.
#     # many=True потрібен для серіалізації QuerySet, а не одного об'єкта.
#     # Response повертає список у JSON зі статусом 200 OK.
#     def get(self, request):
#         books = BookModel.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     # POST /api/books/
#     # request.data містить дані, отримані від клієнта.
#     # is_valid() перевіряє їх відповідність правилам серіалізатора.
#     # save() створює новий запис у базі даних.
#     # Успіх — 201 Created, помилка валідації — 400 Bad Request.
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Обробляє запити до конкретної книги за її первинним ключем (pk).
# class BookDetailView(APIView):
#     # Шукає книгу за pk, отриманим із URL.
#     # Якщо запису немає, Django генерує Http404,
#     # який DRF перетворює на відповідь 404 Not Found.
#     def get_object(self, pk):
#         return get_object_or_404(BookModel, pk=pk)

#     # GET /api/books/<pk>/
#     # Серіалізує один знайдений об'єкт і повертає 200 OK.
#     def get(self, request, pk):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)

#     # PUT /api/books/<pk>/
#     # Повне оновлення: клієнт передає всі обов'язкові поля.
#     # serializer.save() викликає update() для наявного об'єкта.
#     # Успіх — 200 OK, невалідні дані — 400 Bad Request.
#     def put(self, request, pk):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # PATCH /api/books/<pk>/
#     # Часткове оновлення: partial=True дозволяє передати
#     # лише ті поля, значення яких потрібно змінити.
#     # Успіх — 200 OK, помилка валідації — 400 Bad Request.
#     def patch(self, request, pk):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # DELETE /api/books/<pk>/
#     # Видаляє знайдений об'єкт із бази даних.
#     # Повертає 204 No Content без тіла відповіді.
#     def delete(self, request, pk):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )

# from apps.books.filter import filter_books

# from .models import BookModel
# from .serializers import BookSerializer


# # Готовий клас DRF для отримання списку книг і створення нових
# class BookListCreateView(ListCreateAPIView):
#     # Вказуємо серіалізатор для роботи з даними книги
#     serializer_class = BookSerializer

#     # Визначаємо, які книги потрібно отримати з бази даних
#     def get_queryset(self):
#         # Передаємо параметри запиту у функцію фільтрації
#         return filter_books(self.request.query_params)


# # Готовий клас DRF для отримання, оновлення та видалення книги
# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     # Вказуємо серіалізатор для роботи з даними книги
#     serializer_class = BookSerializer

#     # Вказуємо набір книг, серед яких DRF шукатиме потрібну за ID
#     queryset = BookModel.objects.all()
