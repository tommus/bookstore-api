from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from bookstore.bindings.schemas import schema_binding_list_query, schema_binding_list_response, \
    schema_binding_details_path, schema_binding_details_response
from bookstore.bindings.serializers import BindingSerializer
from bookstore.bindings.models import Binding
from bookstore.common.schemas import schema_error


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
        manual_parameters=schema_binding_list_query,
        operation_id="binding:list",
        operation_summary="List bindings (pageable)",
        operation_description="Allows to retrieve a list of bindings.",
        responses={
            HTTP_200_OK: openapi.Response(
                description="Request finished successfully.",
                schema=schema_binding_list_response,
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
        manual_parameters=schema_binding_details_path,
        operation_id="binding:details",
        operation_summary="Binding details",
        operation_description="Allows to retrieve a details on given binding.",
        responses={
            HTTP_200_OK: openapi.Response(
                description="Request finished successfully.",
                schema=schema_binding_details_response,
            ),
            HTTP_404_NOT_FOUND: openapi.Response(
                description="Binding with given `id` not found.",
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
class BindingViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    pagination_class = None
    queryset = Binding.objects.all()
    serializer_class = BindingSerializer
