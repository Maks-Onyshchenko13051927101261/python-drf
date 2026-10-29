from django.db.models import QuerySet
from django.http import QueryDict

from apps.books.models import BookModel


def filter_books(query: QueryDict) -> QuerySet:
    """
    Filters a list of books based on the provided keyword arguments.

    Args:
        query (QueryDict): The query parameters for filtering.
        **kwargs: Arbitrary keyword arguments representing filter criteria.

    Returns:
        QuerySet: A filtered QuerySet of BookModel instances.
    """

    qs = BookModel.objects.all()

    for k, v in query.items():
        match k:
            case "title":
                qs = qs.filter(title__icontains=v)
            case "author":
                qs = qs.filter(author__icontains=v)
            case "genre":
                qs = qs.filter(genre__icontains=v)
            case "publication_year":
                qs = qs.filter(publication_year=v)
            case "isbn":
                qs = qs.filter(isbn__icontains=v)
            case _:
                raise ValueError(f"Invalid filter key: {k}")

    return qs
