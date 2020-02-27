from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from bookstore.author.models import Author
from bookstore.author.serializers import AuthorSerializer
from bookstore.common.pagination import CursorHashPagination


class AuthorPagination(CursorHashPagination):
    page_size = 25


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination

    @swagger_auto_schema(
        operation_id="List authors",
        operation_summary="List authors (pageable)",
        operation_description="Allows to retrieve a list of authors.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="Author details",
        operation_summary="Author details",
        operation_description="Allows to retrieve a details on given author.",
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
