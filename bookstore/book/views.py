from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from bookstore.book.models import Binding, Book
from bookstore.book.serializers import BindingSerializer, BookListSerializer
from bookstore.common.pagination import CursorHashPagination


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
        operation_id="List bindings",
        operation_summary="List bindings (pageable)",
        operation_description="Allows to retrieve a list of bindings.",
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
        operation_id="Binding details",
        operation_summary="Binding details",
        operation_description="Allows to retrieve a details on given binding.",
        tags=["books"],
    )
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(auto_schema=None)
)
class BindingViewSet(viewsets.ModelViewSet):
    queryset = Binding.objects.all()
    serializer_class = BindingSerializer
    pagination_class = None


class BookPagination(CursorHashPagination):
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
        operation_id="List books",
        operation_summary="List books (pageable)",
        operation_description="Allows to retrieve a list of books.",
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
        operation_id="Book details",
        operation_summary="Book details",
        operation_description="Allows to retrieve a details on given book.",
        tags=["books"],
    )
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(auto_schema=None)
)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BookPagination
