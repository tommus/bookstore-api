from django.db.models import Model, DateTimeField


class TimestampModel(Model):
    """Model containing information about entity creation."""

    # Date of creation.
    created = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
