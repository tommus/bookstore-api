from rest_framework import viewsets
from rest_framework.pagination import CursorPagination

from bookstore.publisher.models import Publisher
from bookstore.publisher.serializers import PublisherSerializer


class PublisherPagination(CursorPagination):
    page_size = 25


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = PublisherPagination
