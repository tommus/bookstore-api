from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from bookstore.common.pagination import CursorHashPagination
from bookstore.publisher.models import Publisher
from bookstore.publisher.serializers import PublisherSerializer


class PublisherPagination(CursorHashPagination):
    page_size = 25


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = PublisherPagination

    @swagger_auto_schema(
        operation_id="List publishers",
        operation_summary="List publishers (pageable)",
        operation_description="Allows to retrieve a list of publishers.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="Publisher details",
        operation_summary="Publisher details",
        operation_description="Allows to retrieve a details on given publisher.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
