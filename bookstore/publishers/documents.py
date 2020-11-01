from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.fields import IntegerField
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl_drf.compat import StringField, KeywordField

from bookstore.publishers.models import Publisher


@registry.register_document
class PublisherDocument(Document):
    """Represents publisher as searchable document."""

    # Used to index publisher ids.
    id = IntegerField(attr="id")

    # Publisher's details.
    name = StringField(fields={"raw": KeywordField()})

    class Index:
        """Index configuration."""

        # Defines search engine index for publishers table.
        name = "publishers"

        # Defines additional index settings.
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        """Django integration configuration."""

        # Points to the database model associated with indexing document.
        model = Publisher
