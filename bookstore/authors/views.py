from django.utils.decorators import method_decorator
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
    LOOKUP_FILTER_FUZZY,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_CONTAINS,
    LOOKUP_QUERY_STARTSWITH,
    LOOKUP_QUERY_ENDSWITH,
    SUGGESTER_TERM, SUGGESTER_PHRASE)
from django_elasticsearch_dsl_drf.filter_backends import (
    CompoundSearchFilterBackend,
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    IdsFilterBackend,
    SuggesterFilterBackend
)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from bookstore.authors.documents import AuthorDocument
from bookstore.authors.models import Author
from bookstore.authors.schemas import (
    schema_author_list_query,
    schema_author_list_response,
    schema_author_details_path,
    schema_author_details_response,
)
from bookstore.authors.serializers import AuthorSerializer, AuthorDocumentSerializer
from bookstore.common.pagination import CursorHashPagination
from bookstore.common.schemas import schema_error


class AuthorPagination(CursorHashPagination):
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
        manual_parameters=schema_author_list_query,
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
    name="partial_update",
    decorator=swagger_auto_schema(auto_schema=None)
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
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(auto_schema=None)
)
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination


# TODO: Reveal methods.

# noinspection PyTypeChecker
@method_decorator(
    name="functional_suggest",
    decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="suggest",
    decorator=swagger_auto_schema(auto_schema=None)
)
class AuthorSearchViewSet(DocumentViewSet):
    document = AuthorDocument
    filter_backends = [
        CompoundSearchFilterBackend,
        DefaultOrderingFilterBackend,
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        SuggesterFilterBackend,
    ]
    filter_fields = {
        "id": {
            "field": "id",
            "lookups": [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ]
        },
        "first_name": {
            "field": "first_name.raw",
            "lookups": [
                LOOKUP_FILTER_FUZZY,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_CONTAINS,
                LOOKUP_QUERY_ENDSWITH,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_STARTSWITH,
            ]
        },
        "last_name": "last_name.raw",
    }
    lookup_field = "id"
    ordering = ("id", "first_name", "last_name",)
    ordering_fields = {
        "id": "id",
        "first_name": "first_name.raw",
        "last_name": "last_name.raw",
    }
    pagination_class = PageNumberPagination
    multi_match_search_fields = {
        "first_name": {"boost": 4},
        "last_name": {"boost": 2},
    }
    search_fields = {
        "first_name": {"boost": 4},
        "last_name": {"boost": 2},
    }
    serializer_class = AuthorDocumentSerializer
    suggester_fields = {
        "first_name_suggest": {
            "field": "first_name.suggest",
            "options": {
                "size": 20
            },
            "suggesters": [
                SUGGESTER_COMPLETION,
                SUGGESTER_TERM,
                SUGGESTER_PHRASE,
            ]
        },
        "last_name_suggest": {
            "field": "last_name.suggest",
            "options": {
                "size": 20
            },
            "suggesters": [
                SUGGESTER_COMPLETION,
                SUGGESTER_TERM,
                SUGGESTER_PHRASE,
            ]
        }
    }
