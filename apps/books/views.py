# from django.db.models import Avg, Count, Q
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
#     # # GET /api/books/
#     # # Q дозволяє об'єднувати умови через OR (|).
#     # # exclude() прибирає записи, які відповідають умові.
#     # # order_by() задає порядок результатів.
#     # def get(self, request):
#     #     books = (
#     #         BookModel.objects.filter(
#     #             Q(title__icontains="python") | Q(author__icontains="python")
#     #         )
#     #         .exclude(language="unknown")
#     #         .order_by("title")
#     #     )

#     #     serializer = BookSerializer(books, many=True)
#     #     return Response(serializer.data)

#     # # Перші п'ять книг за назвою (зріз QuerySet).
#     # first_five = BookModel.objects.order_by("title")[:5]

#     # # Отримуємо лише потрібні поля у вигляді словників.
#     # book_data = BookModel.objects.values("title", "author")

#     # # aggregate() обчислює підсумкове значення для всієї вибірки.
#     # stats = BookModel.objects.aggregate(average_pages=Avg("pages"))

#     # # annotate() додає обчислене поле до кожної групи.
#     # authors = (
#     #     BookModel.objects.values("author")
#     #     .annotate(book_count=Count("id"))
#     #     .order_by("-book_count")
#     # )

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


# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import (
#     CreateModelMixin,
#     DestroyModelMixin,
#     ListModelMixin,
#     RetrieveModelMixin,
#     UpdateModelMixin,
# )

# # from rest_framework.response import Response
# from apps.books.filter import filter_books
# from apps.books.models import BookModel
# from apps.books.serializers import BookSerializer


# # GenericAPIView надає базові механізми роботи з queryset,
# # серіалізатором і пошуком об'єктів.
# # Mixins додають готові CRUD-операції, але HTTP-методи
# # ми ще пов'язуємо з ними вручну.
# class BookListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     # queryset = BookModel.objects.all()
#     # DRF використовує цей клас для перетворення моделей у JSON,
#     # перевірки вхідних даних і створення нових записів.
#     serializer_class = BookSerializer

#     # На відміну від статичного атрибута queryset,
#     # get_queryset() виконується під час обробки запиту.
#     # Це дозволяє будувати вибірку залежно від query_params.
#     def get_queryset(self):
#         # Використовуємо функцію filter_books для фільтрації книг за параметрами запиту
#         return filter_books(self.request.query_params)

#     # GET /api/books/
#     # ListModelMixin отримує queryset через get_queryset(),
#     # серіалізує всі знайдені книги з many=True і повертає 200 OK.
#     def get(self, request):
#         return super().list(request)

#     # POST /api/books/
#     # CreateModelMixin перевіряє request.data через серіалізатор,
#     # зберігає валідний об'єкт і повертає 201 Created.
#     # Якщо дані некоректні, DRF повертає 400 Bad Request.
#     def post(self, request):
#         return super().create(request)

#     # def get(self, request):
#     #     qs = BookModel.objects.all()
#     #     serializer = BookSerializer(qs, many=True)
#     #     return Response(serializer.data)

#     # def post(self, request):
#     #     serializer = BookSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data, status=201)


# # GenericAPIView забезпечує пошук об'єкта за pk із URL.
# # Mixins реалізують читання, оновлення та видалення.
# class BookDetailView(
#     GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# ):
#     # Базова вибірка, у якій DRF шукатиме книгу.
#     queryset = BookModel.objects.all()
#     # Серіалізатор використовується для читання й перевірки даних.
#     serializer_class = BookSerializer

#     # GET /api/books/<pk>/
#     # RetrieveModelMixin викликає get_object(), який шукає книгу
#     # за pk у queryset. Якщо її немає — 404, інакше — 200 OK.
#     def get(self, request, pk):
#         return super().retrieve(request, pk=pk)

#     # PUT /api/books/<pk>/
#     # UpdateModelMixin перевіряє повний набір обов'язкових полів
#     # і оновлює знайдений запис. Успіх — 200, помилка даних — 400.
#     def put(self, request, pk):
#         return super().update(request, pk=pk)

#     # PATCH /api/books/<pk>/
#     # partial_update() передає partial=True у серіалізатор,
#     # тому можна оновити лише частину полів. Успіх — 200.
#     def patch(self, request, pk):
#         return super().partial_update(request, pk=pk)

#     # DELETE /api/books/<pk>/
#     # DestroyModelMixin знаходить і видаляє книгу.
#     # Успішна відповідь — 204 No Content без тіла.
#     def delete(self, request, pk):
#         return super().destroy(request, pk=pk)

# def get(self, request, pk):
#     book = self.get_object()
#     serializer = BookSerializer(book)
#     return Response(serializer.data)

# def put(self, request, pk):
#     book = self.get_object()
#     serializer = BookSerializer(book, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)

# def patch(self, request, pk):
#     book = self.get_object()
#     serializer = BookSerializer(book, data=request.data, partial=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)

# def delete(self, request, pk):
#     book = self.get_object()
#     book.delete()
#     return Response(status=204)


from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from apps.books.filter import filter_books

from .models import BookModel
from .serializers import BookSerializer


# ListCreateAPIView об'єднує GenericAPIView із ListModelMixin
# та CreateModelMixin і автоматично обробляє:
# GET /api/books/ — повертає список книг зі статусом 200 OK.
# POST /api/books/ — перевіряє дані серіалізатором і створює
# запис зі статусом 201 Created або повертає 400 Bad Request.
class BookListCreateView(ListCreateAPIView):
    # ModelSerializer перетворює об'єкти моделі на дані відповіді
    # та перевіряє вхідні дані перед створенням запису.
    serializer_class = BookSerializer

    # get_queryset() викликається під час обробки запиту,
    # тому дозволяє врахувати параметри фільтрації з URL.
    # На відміну від атрибута queryset, вибірка тут формується
    # динамічно для поточного запиту.
    def get_queryset(self):
        return filter_books(self.request.query_params)


# RetrieveUpdateDestroyAPIView об'єднує GenericAPIView
# із RetrieveModelMixin, UpdateModelMixin та DestroyModelMixin.
# Автоматично обробляє:
# GET — отримання книги (200 OK).
# PUT — повне оновлення (200 OK).
# PATCH — часткове оновлення (200 OK).
# DELETE — видалення (204 No Content).
# get_object() шукає книгу за pk з URL у queryset.
# Якщо запис відсутній, DRF повертає 404 Not Found.
# Некоректні дані для PUT/PATCH повертають 400 Bad Request.
class BookDetailView(RetrieveUpdateDestroyAPIView):
    # Серіалізатор відповідає за читання, перевірку й оновлення даних.
    serializer_class = BookSerializer

    # Базова вибірка, в якій get_object() шукає книгу за pk.
    queryset = BookModel.objects.all()
