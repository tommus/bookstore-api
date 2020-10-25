from django.db import models


class Binding(models.Model):
    """Description."""
    description = models.CharField(max_length=255, unique=True)

    """Created."""
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
