from django.utils.decorators import method_decorator
from django_elasticsearch_dsl_drf.filter_backends import OrderingFilterBackend, DefaultOrderingFilterBackend, \
    CompoundSearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from bookstore.books.documents import BookDocument
from bookstore.books.schemas import (
    schema_book_list_response,
    schema_book_details_path,
    schema_book_details_response,
)
from bookstore.books.serializers import BookListSerializer, BookDetailsSerializer
from bookstore.common.pagination import LimitOffsetPagination
from bookstore.common.schemas import schema_error


class BookPagination(LimitOffsetPagination):
    max_limit = 50


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
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
class BookViewSet(BaseDocumentViewSet):
    """A view set that provides CRUD methods configuration
    for book document."""

    # Associates view set with book document.
    document = BookDocument

    # Defines what sort of filtering options are available.
    filter_backends = [
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend
    ]

    # Defines a single document lookup field.
    lookup_field = "id"

    # Defines which fields will be searched against.
    multi_match_search_fields = (
        "title", "author_indexing", "publisher_indexing", "isbn", "ean", "description")

    # Defines item ordering.
    ordering = ("id", "title", "author_indexing", "publisher_indexing")
    ordering_fields = {
        "id": "id",
        "title": "title.raw",
        "author": "author_indexing.raw",
        "publisher": "publisher_indexing.raw"
    }

    # Defines which fields will be searched against.
    search_fields = (
        "title", "author_indexing", "publisher_indexing", "isbn", "ean", "description")

    # Configures pagination.
    pagination_class = BookPagination

    # Configures serialization.
    serializers = {
        "list": BookListSerializer,
        "retrieve": BookDetailsSerializer
    }

    def get_serializer_class(self):
        return self.serializers[self.action]
