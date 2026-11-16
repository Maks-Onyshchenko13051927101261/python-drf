from datetime import date

from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.books.models import BookModel


def filter_books(query: QueryDict) -> QuerySet:
    """
    Формує QuerySet за параметрами URL.
    Некоректні параметри повертають клієнту HTTP 400.
    """
    qs = BookModel.objects.all()

    for k, v in query.items():
        match k:
            case "title":
                qs = qs.filter(title__icontains=v)

            case "author":
                qs = qs.filter(author__icontains=v)

            case "published_date":
                try:
                    date.fromisoformat(v)
                except ValueError:
                    raise ValidationError({k: "Очікується дата y форматі YYYY-MM-DD."})
                qs = qs.filter(published_date=v)

            case "isbn":
                qs = qs.filter(isbn__icontains=v)

            case "language":
                qs = qs.filter(language__icontains=v)

            case "pages":
                if not v.isdecimal():
                    raise ValidationError({k: "Очікується невід'ємне ціле число."})
                qs = qs.filter(pages=int(v))

            case _:
                raise ValidationError({k: f"Невідомий параметр фільтрації: {k}."})

    return qs
