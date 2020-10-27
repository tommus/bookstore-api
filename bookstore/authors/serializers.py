from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from bookstore.authors.documents import AuthorDocument
from bookstore.authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """Serializes author model."""

    class Meta:
        """Describes serialization details."""

        # Points to the entity associated with this serializer.
        model = Author

        # Defines which fields will be serialized.
        fields = ("id", "first_name", "last_name")


class AuthorDocumentSerializer(DocumentSerializer):
    """Serializes author document."""

    class Meta:
        """Describes serialization details."""

        # Points to the document associated with this serializer.
        document = AuthorDocument
