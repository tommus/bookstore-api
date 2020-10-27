from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.fields import IntegerField
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl_drf.compat import StringField, KeywordField

from bookstore.authors.models import Author


@registry.register_document
class AuthorDocument(Document):
    """Represents author of the books as searchable document."""

    # Used to index author ids.
    id = IntegerField(attr="id")

    # Author's personal details.
    first_name = StringField(fields={"raw": KeywordField()})
    last_name = StringField(fields={"raw": KeywordField()})

    class Index:
        """Index configuration."""

        # Defines search engine index for authors table.
        name = "authors"

        # Defines additional index settings.
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        """Django integration configuration."""

        # Points to the database model associated with indexing document.
        model = Author
