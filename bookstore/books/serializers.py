from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from bookstore.books.documents import BookDocument


class BookListSerializer(DocumentSerializer):
    """Serializes book documents into a list."""

    class Meta:
        """Describes serialization details."""

        # Points to the document associated with this serializer.
        document = BookDocument

        # Defines which fields are subject for serialization.
        fields = ("id", "title", "author", "publisher", "publication_year", "cover")


class BookDetailsSerializer(DocumentSerializer):
    """Serializes book document into detailed view."""

    class Meta:
        """Describes serialization details."""

        # Points to the document associated with this serializer.
        document = BookDocument

        # Defines which fields are subject for serialization.
        fields = (
            "id", "title", "author", "publisher", "publication_year", "binding", "pages", "cover",
            "format", "isbn", "ean", "release_date", "available", "price_base", "price_discounted",
            "description"
        )
