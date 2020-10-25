from rest_framework import serializers

from bookstore.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes book model.
    """

    cover = serializers.SerializerMethodField("get_cover_url")

    def get_cover_url(self, obj):

        if not obj.cover:
            return obj.cover_url
        else:
            request = self.context.get("request")
            url = obj.cover.url
            return request.build_absolute_uri(url)


class BookListSerializer(BookSerializer):
    """
    Serializes book models into a list.
    """

    class Meta:
        model = Book
        fields = ("id", "title", "author", "publisher", "publication_year", "cover",)


class BookDetailsSerializer(BookSerializer):
    """
    Serializes book model into detailed view.
    """

    class Meta:
        model = Book
        fields = (
            "id", "title", "author", "publisher", "publication_year", "binding", "pages", "cover",
            "format", "isbn", "ean", "release_date", "available", "price_base", "price_discounted",
            "description"
        )
