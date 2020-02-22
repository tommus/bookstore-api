from rest_framework import serializers

from bookstore.author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes author model.
    """

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name",)
