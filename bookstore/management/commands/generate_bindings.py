from django.core.management import BaseCommand
from django.db import IntegrityError

from bookstore.models import Binding

# region Constants

DEFAULT_COUNT = 25

# endregion


# region Sample

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


# endregion

# region Command

class Command(BaseCommand):
    """
    Implements Django management command and allows to generate sample binding entities.
    """

    # region Documentation

    help = "Generates sample bindings."

    # endregion

    # region Handler

    def handle(self, *args, **options):
        """
        Generates given number of bindings.
        """

        for description in BINDINGS:
            """Persists author in database."""
            try:
                Binding.objects.create(description=description)
            except IntegrityError:
                """Silently ignore duplicates."""
                pass

    # endregion

# endregion
