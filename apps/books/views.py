from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from apps.books.filter import filter_books

from .models import BookModel
from .serializers import BookSerializer


class BookListCreateView(ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return filter_books(self.request.query_params)


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
