from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from bookstore.book.models import Binding, Book
from bookstore.book.serializers import BindingSerializer, BookListSerializer, BookDetailsSerializer
from bookstore.common.pagination import CursorHashPagination


class BindingViewSet(viewsets.ModelViewSet):
    queryset = Binding.objects.all()
    serializer_class = BindingSerializer
    pagination_class = None

    @swagger_auto_schema(
        operation_id="List bindings",
        operation_summary="List bindings (pageable)",
        operation_description="Allows to retrieve a list of bindings.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="Binding details",
        operation_summary="Binding details",
        operation_description="Allows to retrieve a details on given binding.",
    )
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = BookDetailsSerializer
        return super(BookViewSet, self).retrieve(request, *args, **kwargs)

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


class BookPagination(CursorHashPagination):
    page_size = 25


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BookPagination

    @swagger_auto_schema(
        operation_id="List books (pageable)",
        operation_summary="List books (pageable)",
        operation_description="Allows to retrieve a list of books.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="Book details",
        operation_summary="Book details",
        operation_description="Allows to retrieve a details on given book."
    )
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = BookDetailsSerializer
        return super(BookViewSet, self).retrieve(request, *args, **kwargs)

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
