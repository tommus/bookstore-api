from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from bookstore.books.models import Book


class CartStatus(Enum):
    """Describes a cart status."""

    # Possible cart statuses.
    NEW = _("New")
    CART = _("Cart")
    CHECKOUT = _("Checkout")
    PAID = _("Paid")
    COMPLETE = _("Complete")
    ABANDONED = _("Abandoned")

    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]


class Cart(models.Model):
    """Represents cart"""

    # Reference to identify the user associated with the cart.
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, related_name="carts")

    # Unique token to identify the cart.
    token = models.CharField(max_length=100)

    # The status of the cart.
    status = models.CharField(
        max_length=10, choices=CartStatus.choices(), default=CartStatus.NEW)

    # The details of the user.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # Contact details of the user.
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    # Address details of the user.
    line_1 = models.CharField(max_length=50)
    line_2 = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    # Availability details.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Represents this entity as a char sequence."""

        # Concatenate user and token.
        return "{} - {}".format(self.user, self.token)


class CartItem(models.Model):
    """Represents a single cart item."""

    # Reference to identify the book associated with a cart item.
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE, related_name="cart_items")

    # Reference to identify the cart associated with a cart item.
    cart = models.ForeignKey(
        to=Cart, on_delete=models.CASCADE, related_name="cart_items")

    # The stock keeping unit used while purchasing the item.
    sku = models.CharField(max_length=50, null=True)

    # The price of the item while purchasing the item.
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # The discount of the product while purchasing the item.
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # The quantity of the item selected by user.
    quantity = models.SmallIntegerField(default=0)

    # The flag to identify whether a product is active on the cart.
    active = models.BooleanField(default=True)

    # Availability details.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Represents this entity as a char sequence."""

        # Concatenate user and token.
        return "{} - {}".format(self.cart, self.book)
