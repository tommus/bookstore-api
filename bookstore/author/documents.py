from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from bookstore.author.models import Author


@registry.register_document
class AuthorDocument(Document):
    """
    Search supported document for authors index.
    """

    id = fields.IntegerField(attr="id")

    first_name = fields.TextField(
        attr="first_name",
        fields={
            "raw": fields.TextField(analyzer="keyword", fielddata=True),
            "suggest": fields.Completion()
        }
    )

    last_name = fields.TextField(
        attr="last_name",
        fields={
            "raw": fields.TextField(analyzer="keyword", fielddata=True),
            "suggest": fields.Completion()
        }
    )

    created = fields.DateField(attr="created")

    class Django:
        model = Author

    class Index:
        name = "author"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
