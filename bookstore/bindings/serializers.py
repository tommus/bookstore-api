from rest_framework import serializers

from bookstore.bindings.models import Binding


class BindingSerializer(serializers.ModelSerializer):
    """Serializes binding model."""

    class Meta:
        model = Binding
        fields = ("id", "description",)
