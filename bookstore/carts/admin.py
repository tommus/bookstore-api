from django.contrib import admin
from django.contrib.admin import register

from bookstore.carts.models import Cart


@register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Configures application's admin panel."""

    # Specifies which fields will be shown at list view.
    list_display = ("user", "token")

    # Configures admin panel's pagination.
    list_per_page = 100

    # Defines searching and sorting.
    search_fields = ("user", "token", "mobile", "email")
    sortable_by = ("user", "created", "updated")
