from django.db import models

from bookstore.authors.models import Author
from bookstore.bindings.models import Binding
from bookstore.publishers.models import Publisher


class Book(models.Model):
    """Title."""
    title = models.CharField(max_length=255)

    """Author"""
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name="books")

    """Publisher."""
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, related_name="books")

    """Publication year."""
    publication_year = models.PositiveSmallIntegerField()

    """Binding."""
    binding = models.ForeignKey(to=Binding, on_delete=models.CASCADE, related_name="books")

    """Number of pages."""
    pages = models.PositiveSmallIntegerField()

    """Size format."""
    format = models.CharField(max_length=255)

    """ISBN number."""
    isbn = models.CharField(max_length=31)

    """EAN code."""
    ean = models.CharField(max_length=31)

    """Release date."""
    release_date = models.DateField()

    """Available stock."""
    available = models.PositiveSmallIntegerField()

    """Price base."""
    price_base = models.DecimalField(max_digits=8, decimal_places=2)

    """Price discounted."""
    price_discounted = models.DecimalField(max_digits=8, decimal_places=2)

    """Description."""
    description = models.TextField(max_length=4095)

    """Cover image."""
    cover = models.ImageField(upload_to="covers", blank=True, null=True)

    """Cover url."""
    cover_url = models.URLField(default="", blank=True)

    """Created."""
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.author)