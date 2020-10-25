from django.db import models


class Author(models.Model):
    """First name."""
    first_name = models.CharField(max_length=255)

    """Last name."""
    last_name = models.CharField(max_length=255)

    """Created."""
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
