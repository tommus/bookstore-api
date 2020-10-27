from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from bookstore.authors.documents import AuthorDocument


class AuthorSerializer(DocumentSerializer):
    """Serializes author document."""

    class Meta:
        """Describes serialization details."""

        # Points to the document associated with this serializer.
        document = AuthorDocument
