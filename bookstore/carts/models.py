from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


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
