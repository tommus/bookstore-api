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
