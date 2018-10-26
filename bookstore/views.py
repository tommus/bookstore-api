from rest_framework import viewsets
from rest_framework.pagination import CursorPagination

from bookstore.models import Author, Binding, Book, Publisher
from bookstore.serializers import AuthorSerializer, BindingSerializer, PublisherSerializer, \
    BookDetailsSerializer, BookListSerializer


# region Author

class AuthorPagination(CursorPagination):
    page_size = 100


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination


# endregion

# region Binding


class BindingViewSet(viewsets.ModelViewSet):
    queryset = Binding.objects.all()
    serializer_class = BindingSerializer
    pagination_class = None


# endregion

# region Book

class BookPagination(CursorPagination):
    page_size = 100


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BookPagination

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = BookDetailsSerializer
        return super(BookViewSet, self).retrieve(request, *args, **kwargs)


# endregion

# region Publisher

class PublisherPagination(CursorPagination):
    page_size = 100


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = PublisherPagination

# endregion
