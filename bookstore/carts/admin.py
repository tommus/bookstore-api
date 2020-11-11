from django.contrib import admin
from django.contrib.admin import register

from bookstore.carts.models import Cart, CartItem


@register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Configures application's admin panel."""

    # Specifies which fields will be shown at list view.
    list_display = ("user", "token")

    # Configures admin panel's pagination.
    list_per_page = 100

    # Defines searching and sorting.
    search_fields = ("user__email", "user__first_name", "user__last_name",
                     "token", "mobile", "email")
    sortable_by = ("user", "created", "updated")


@register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """Configures application's admin panel."""

    # Specifies which fields will be shown at list view.
    list_display = ("cart", "book", "price", "discount", "quantity", "active")

    # Configures admin panel's pagination.
    list_per_page = 100

    # Defines searching and sorting.
    search_fields = ("book__title", "book__author__first_name",
                     "book__author__last_name", "book__publisher__name")
    sortable_by = ("cart", "price", "discount", "quantity", "active")
