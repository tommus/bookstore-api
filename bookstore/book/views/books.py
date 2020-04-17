from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from bookstore.book.models import Book
from bookstore.book.schemas.books import (
    schema_book_list_query,
    schema_book_list_response,
    schema_book_details_path,
    schema_book_details_response,
)
from bookstore.book.serializers import BookListSerializer
from bookstore.common.pagination import CursorHashPagination
from bookstore.common.schemas import schema_error


class BookPagination(CursorHashPagination):
    page_size = 25


# noinspection PyTypeChecker
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        manual_parameters=schema_book_list_query,
        operation_id="book:list",
        operation_summary="List books (pageable)",
        operation_description="Allows to retrieve a list of books.",
        responses={
            HTTP_200_OK: openapi.Response(
                description="Request finished successfully.",
                schema=schema_book_list_response,
            ),
        },
        security=[],
        tags=["books"],
    )
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        manual_parameters=schema_book_details_path,
        operation_id="book:details",
        operation_summary="Book details",
        operation_description="Allows to retrieve a details on given book.",
        responses={
            HTTP_200_OK: openapi.Response(
                description="Request finished successfully.",
                schema=schema_book_details_response,
            ),
            HTTP_404_NOT_FOUND: openapi.Response(
                description="Book with given `id` not found.",
                schema=schema_error("not_found"),
            ),
        },
        security=[],
        tags=["books"],
    )
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(auto_schema=None)
)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BookPagination
