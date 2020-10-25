from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from bookstore.authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes author model.
    """

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name",)


# class AuthorDocumentSerializer(DocumentSerializer):
#     class Meta:
#         document = AuthorDocument
#         fields = (
#             "id",
#             "first_name",
#             "last_name",
#         )
