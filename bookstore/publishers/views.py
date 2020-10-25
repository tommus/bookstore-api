from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from bookstore.common.pagination import CursorHashPagination
from bookstore.common.schemas import schema_error
from bookstore.publishers.models import Publisher
from bookstore.publishers.schemas import schema_publisher_list_query, schema_publisher_list_response, \
    schema_publisher_details_path, schema_publisher_details_response
from bookstore.publishers.serializers import PublisherSerializer


class PublisherPagination(CursorHashPagination):
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
    name="partial_update",
    decorator=swagger_auto_schema(auto_schema=None)
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
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(auto_schema=None)
)
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = PublisherPagination
