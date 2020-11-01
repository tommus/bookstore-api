from django.contrib import admin
from django.contrib.admin import register

from bookstore.authors.models import Author


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Configures application's admin panel."""

    # Specifies which fields will be shown at list view.
    list_display = ["first_name", "last_name"]

    # Configures admin panel's pagination.
    list_per_page = 100

    # Defines searching and sorting.
    search_fields = ["first_name", "last_name"]
    sortable_by = ["first_name", "last_name"]
