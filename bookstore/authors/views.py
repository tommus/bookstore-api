from django.utils.decorators import method_decorator
from django_elasticsearch_dsl_drf.filter_backends import CompoundSearchFilterBackend, DefaultOrderingFilterBackend, \
    OrderingFilterBackend
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from bookstore.authors.documents import AuthorDocument
from bookstore.authors.schemas import (
    schema_author_list_response,
    schema_author_details_path,
    schema_author_details_response,
)
from bookstore.authors.serializers import AuthorSerializer
from bookstore.common.pagination import LimitOffsetPagination
from bookstore.common.schemas import schema_error


class AuthorPagination(LimitOffsetPagination):
    max_limit = 50


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="author:list",
        operation_summary="List authors (pageable)",
        operation_description="Allows to retrieve a list of authors.",
        responses={
            HTTP_200_OK: openapi.Response(
                description="Request finished successfully.",
                schema=schema_author_list_response,
            ),
        },
        security=[],
        tags=["authors"],
    )
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        manual_parameters=schema_author_details_path,
        operation_id="author:details",
        operation_summary="Author details",
        operation_description="Allows to retrieve a details on given author.",
        responses={
            HTTP_200_OK: openapi.Response(
                description="Request finished successfully.",
                schema=schema_author_details_response,
            ),
            HTTP_404_NOT_FOUND: openapi.Response(
                description="Author with given `id` not found.",
                schema=schema_error("not_found"),
            ),
        },
        security=[],
        tags=["authors"],
    )
)
class AuthorViewSet(BaseDocumentViewSet):
    """A view set that provides CRUD methods configuration for author
    document."""

    # Associates view set with author document.
    document = AuthorDocument

    # Defines what sort of filtering options are available.
    filter_backends = [
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend
    ]

    # Defines a single document lookup field.
    lookup_field = "id"

    # Defines which fields will be searched against.
    multi_match_search_fields = ("first_name", "last_name")

    # Defines item ordering.
    ordering = ("id", "first_name", "last_name")
    ordering_fields = {
        "id": "id",
        "first_name": "first_name.raw",
        "last_name": "last_name.raw"
    }

    # Defines which fields will be searched against.
    search_fields = ("first_name", "last_name")

    # Configures pagination and serialization.
    pagination_class = AuthorPagination
    serializer_class = AuthorSerializer
