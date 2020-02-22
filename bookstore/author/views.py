from rest_framework import viewsets
from rest_framework.pagination import CursorPagination

from bookstore.author.models import Author
from bookstore.author.serializers import AuthorSerializer


class AuthorPagination(CursorPagination):
    page_size = 25


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
