from rest_framework import serializers

from bookstore.models import Author, Binding, Book, Publisher


# region Author Serializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


# endregion

# region Binding Serializer

class BindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Binding
        fields = "__all__"


# endregion

# region Book Serializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


# endregion

# region Publisher Serializer

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"

# endregion
