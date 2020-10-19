from rest_framework import serializers

from bookstore.publisher.models import Publisher


class PublisherSerializer(serializers.ModelSerializer):
    """
    Serializes publisher model.
    """

    class Meta:
        model = Publisher
        fields = ("id", "name",)
