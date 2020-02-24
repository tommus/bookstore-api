from rest_framework import viewsets

from bookstore.book.models import Binding, Book
from bookstore.book.serializers import BindingSerializer, BookListSerializer, BookDetailsSerializer
from bookstore.common.pagination import CursorHashPagination


class BindingViewSet(viewsets.ModelViewSet):
    queryset = Binding.objects.all()
    serializer_class = BindingSerializer
    pagination_class = None


class BookPagination(CursorHashPagination):
    page_size = 25


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BookPagination

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = BookDetailsSerializer
        return super(BookViewSet, self).retrieve(request, *args, **kwargs)
