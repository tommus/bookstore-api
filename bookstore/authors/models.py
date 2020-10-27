from django.db import models

from bookstore.common.models import TimestampModel


class Author(TimestampModel):
    """Represents author of the book."""

    # Author's personal details.
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
