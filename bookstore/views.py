from rest_framework import viewsets

from bookstore.models import Author, Binding, Book, Publisher
from bookstore.serializers import AuthorSerializer, BindingSerializer, BookSerializer, PublisherSerializer


# region Author

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# endregion

# region Binding

class BindingViewSet(viewsets.ModelViewSet):
    queryset = Binding.objects.all()
    serializer_class = BindingSerializer


# endregion

# region Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# endregion

# region Publisher

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

# endregion
