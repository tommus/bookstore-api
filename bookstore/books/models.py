from django.db import models

from bookstore.authors.models import Author
from bookstore.bindings.models import Binding
from bookstore.publishers.models import Publisher


class Book(models.Model):
    """Represents book."""

    # Book's title.
    title = models.CharField(max_length=255)

    # References book's author.
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name="books")

    # References book's publisher.
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, related_name="books")

    # Publication details.
    release_date = models.DateField()
    publication_year = models.PositiveSmallIntegerField()

    # Technical details.
    format = models.CharField(max_length=255)
    pages = models.PositiveSmallIntegerField()
    binding = models.ForeignKey(to=Binding, on_delete=models.CASCADE, related_name="books")

    # Cover image referenced as image or url.
    cover_url = models.URLField(default="", blank=True)
    cover = models.ImageField(upload_to="covers", blank=True, null=True)

    # Book's identifiers.
    isbn = models.CharField(max_length=31)
    ean = models.CharField(max_length=31)

    # Pricing details.
    price_base = models.DecimalField(max_digits=8, decimal_places=2)
    price_discounted = models.DecimalField(max_digits=8, decimal_places=2)

    # Brief description of the book.
    description = models.TextField(max_length=4095)

    # Availability details.
    available = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def author_indexing(self):
        """Author for Elasticsearch indexing."""

        if self.author is not None:
            return self.author.__str__()

    def publisher_indexing(self):
        """Publisher for Elasticsearch indexing."""

        if self.publisher is not None:
            return self.publisher.__str__()

    def binding_indexing(self):
        """Binding for Elasticsearch indexing."""

        if self.binding is not None:
            return self.binding.description

    def cover_indexing(self):
        """Cover url for Elasticsearch indexing."""

        if self.cover_url is not None:
            return self.cover_url

        if self.cover:
            return self.cover.url

    def __str__(self):
        """Represents this entity as a char sequence."""

        # Concatenate title and author.
        return "{} - {}".format(self.title, self.author)
