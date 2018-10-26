from rest_framework import serializers

from bookstore.models import Author, Binding, Book, Publisher


# region Author Serializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name",)


# endregion

# region Binding Serializer

class BindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Binding
        fields = ("id", "description",)


# endregion

# region Book Serializer

class BookSerializer(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField("get_cover_url")

    def get_cover_url(self, obj):

        if not obj.cover:
            return obj.cover_url
        else:
            request = self.context.get("request")
            url = obj.cover.url
            return request.build_absolute_uri(url)


class BookListSerializer(BookSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "publisher", "publication_year", "cover",)


class BookDetailsSerializer(BookSerializer):
    class Meta:
        model = Book
        fields = (
            "id", "title", "author", "publisher", "publication_year", "binding", "pages",
            "format", "isbn", "ean", "release_date", "available", "price_base", "price_discounted",
            "description", "cover"
        )


# endregion

# region Publisher Serializer

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ("id", "name",)

# endregion
