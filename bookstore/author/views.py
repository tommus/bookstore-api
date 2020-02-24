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
