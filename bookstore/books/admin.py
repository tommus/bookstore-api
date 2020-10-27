from django.contrib import admin
from django.contrib.admin import register

from bookstore.books.models import Book


@register(Book)
class BookAdmin(admin.ModelAdmin):
    """Configures application's admin panel."""

    # Specifies which fields will be shown at list view.
    list_display = ("title", "author", "publisher", "binding", "release_date", "available")

    # Configures admin panel's pagination.
    list_per_page = 100

    # Defines searching and sorting.
    search_fields = ("title", "author__first_name", "author__last_name", "publisher__name")
    sortable_by = ("title", "author", "publisher", "binding", "release_date", "available",)
