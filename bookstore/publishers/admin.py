from django.contrib import admin
from django.contrib.admin import register

from bookstore.publishers.models import Publisher


@register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    """Configures application's admin panel."""

    # Specifies which fields will be shown at list view.
    list_display = ["name"]

    # Configures admin panel's pagination.
    list_per_page = 100

    # Defines searching and sorting.
    search_fields = ["name"]
    sortable_by = ["name"]
