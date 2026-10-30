from django.db.models import QuerySet
from django.http import QueryDict

from apps.books.models import BookModel


def filter_books(query: QueryDict) -> QuerySet:
    """
    Фільтрує книги за параметрами запиту.
    Повертає QuerySet із книгами, що відповідають умовам.
    """

    # Отримуємо QuerySet усіх книг
    qs = BookModel.objects.all()

    # Перебираємо параметри, передані в URL
    for k, v in query.items():
        match k:
            case "title":
                # Шукаємо книги за частиною назви без урахування регістру
                qs = qs.filter(title__icontains=v)

            case "author":
                # Шукаємо книги за частиною імені автора
                qs = qs.filter(author__icontains=v)

            case "published_date":
                # Фільтруємо книги за точною датою публікації
                qs = qs.filter(published_date=v)

            case "isbn":
                # Шукаємо книги за ISBN
                qs = qs.filter(isbn__icontains=v)

            case "language":
                # Шукаємо книги за мовою
                qs = qs.filter(language__icontains=v)

            case "pages":
                # Фільтруємо книги за кількістю сторінок
                qs = qs.filter(pages=v)

            case _:
                # Повідомляємо про невідомий параметр фільтрації
                raise ValueError(f"Invalid filter key: {k}")

    # Повертаємо відфільтрований QuerySet
    return qs
