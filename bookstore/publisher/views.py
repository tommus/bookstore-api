from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from bookstore.common.pagination import CursorHashPagination
from bookstore.publisher.models import Publisher
from bookstore.publisher.serializers import PublisherSerializer


class PublisherPagination(CursorHashPagination):
    page_size = 25


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
        operation_id="List publishers",
        operation_summary="List publishers (pageable)",
        operation_description="Allows to retrieve a list of publishers.",
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
        operation_id="Publisher details",
        operation_summary="Publisher details",
        operation_description="Allows to retrieve a details on given publisher.",
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
