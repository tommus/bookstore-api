from django.db import models

from bookstore.common.models import TimestampModel


class Publisher(TimestampModel):
    """Represents publisher."""

    # Publisher's name.
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """Represents this entity as a char sequence."""
        return self.name
