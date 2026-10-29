from django.db import models

from core.models import CoreConfig


class BookModel(CoreConfig):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.title
