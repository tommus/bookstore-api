from django.core.management import BaseCommand
from django.db import IntegrityError

from bookstore.books.models import Binding

BINDINGS = [
    "Saddle Stitched",
    "Loop Stitched",
    "Stab Stitched",
    "Side Stitched",
    "Sewn Bound",
    "Perfect Bound",
    "Tape Bound",
    "Screw Bound",
    "Hardcover",
    "Case Bound",
    "Plastic Grip",
    "Comb Bound",
    "Plastic Bound",
    "Spiral Bound",
    "Coil Bound",
    "Wire-O Bound",
    "Wire Bound"
]


class Command(BaseCommand):
    """
    Implements Django management command and allows to generate sample binding entities.
    """

    help = "Generates sample bindings."

    def handle(self, *args, **options):
        """
        Fills database with sample bindings.
        """

        for description in BINDINGS:
            """Persists author in database."""
            try:
                Binding.objects.create(description=description)
            except IntegrityError:
                """Silently ignore duplicates."""
                pass
