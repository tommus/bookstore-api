from django.utils.decorators import method_decorator
from django_elasticsearch_dsl_drf.filter_backends import OrderingFilterBackend, DefaultOrderingFilterBackend, \
    CompoundSearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from bookstore.common.pagination import LimitOffsetPagination
from bookstore.common.schemas import schema_error
from bookstore.publishers.documents import PublisherDocument
from bookstore.publishers.schemas import schema_publisher_list_query, schema_publisher_list_response, \
    schema_publisher_details_path, schema_publisher_details_response
from bookstore.publishers.serializers import PublisherSerializer


class PublisherPagination(LimitOffsetPagination):
    max_limit = 50


# noinspection PyTypeChecker
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        manual_parameters=schema_publisher_list_query,
        operation_id="publisher:list",
        operation_summary="List publishers (pageable)",
        operation_description="Allows to retrieve a list of publishers.",
        responses={
            HTTP_200_OK: openapi.Response(
                description="Request finished successfully.",
                schema=schema_publisher_list_response,
            ),
        },
        security=[],
        tags=["publishers"],
    )
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        manual_parameters=schema_publisher_details_path,
        operation_id="publisher:details",
        operation_summary="Publisher details",
        operation_description="Allows to retrieve a details on given publisher.",
        responses={
            HTTP_200_OK: openapi.Response(
                description="Request finished successfully.",
                schema=schema_publisher_details_response,
            ),
            HTTP_404_NOT_FOUND: openapi.Response(
                description="Publisher with given `id` not found.",
                schema=schema_error("not_found"),
            ),
        },
        security=[],
        tags=["publishers"],
    )
)
class PublisherViewSet(BaseDocumentViewSet):
    """A view set that provides CRUD methods configuration
    for publisher document."""

    # Associates view set with publisher document.
    document = PublisherDocument

    # Defines what sort of filtering options are available.
    filter_backends = [
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend
    ]

    # Defines a single document lookup field.
    lookup_field = "id"

    # Defines item ordering.
    ordering = ("id", "name")
    ordering_fields = {
        "id": "id",
        "name": "name.raw"
    }

    # Defines which fields will be searched against.
    search_fields = ["name"]

    # Configures pagination.
    pagination_class = PublisherPagination

    # Configures serialization.
    serializer_class = PublisherSerializer
