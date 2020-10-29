from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.fields import IntegerField, DateField, FloatField
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl_drf.compat import StringField, KeywordField

from bookstore.books.models import Book


@registry.register_document
class BookDocument(Document):
    """Represents book as searchable document."""

    # Used to index book ids.
    id = IntegerField(attr="id")

    # Book's title.
    title = StringField(fields={"raw": KeywordField()})

    # References book's author.
    author = IntegerField(attr="author.id")
    author_indexing = StringField(
        attr="author_indexing",
        fields={"raw": KeywordField()}
    )

    # References book's publisher.
    publisher = IntegerField(attr="publisher.id")
    publisher_indexing = StringField(
        attr="publisher_indexing",
        fields={"raw": KeywordField()}
    )

    # Publication details.
    release_date = DateField()
    publication_year = IntegerField()

    # Technical details.
    format = StringField(fields={"raw": KeywordField()})
    pages = IntegerField()
    binding = IntegerField(attr="binding.id")
    binding_indexing = StringField(
        attr="binding_indexing",
        fields={"raw": KeywordField()}
    )

    # Cover image referenced as image or url.
    cover = StringField(attr="cover_indexing")

    # Book's identifiers.
    isbn = StringField(fields={"raw": KeywordField()})
    ean = StringField(fields={"raw": KeywordField()})

    # Pricing details.
    price_base = FloatField()
    price_discounted = FloatField()

    # Brief description of the book.
    description = StringField(fields={"raw": KeywordField()})

    # Availability details.
    available = IntegerField()
    created = DateField()

    class Index:
        """Index configuration."""

        # Defines search engine index for books table.
        name = "books"

        # Defines additional index settings.
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        """Django integration configuration."""

        # Points to the database model associated with indexing document.
        model = Book
