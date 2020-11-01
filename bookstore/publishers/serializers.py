from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from bookstore.publishers.documents import PublisherDocument


class PublisherSerializer(DocumentSerializer):
    """Serializes publisher document."""

    class Meta:
        """Describes serialization details."""

        # Points to the document associated with this serializer.
        document = PublisherDocument

        # Defines which fields are subject for serialization.
        fields = ("id", "name")
