from django.core.management import BaseCommand
from django.db import IntegrityError
from faker import Factory
from faker.providers import company

from bookstore.publisher.models import Publisher

DEFAULT_COUNT = 25

fake = Factory.create()
fake.add_provider(company)


class Command(BaseCommand):
    """
    Implements Django management command and allows to generate sample publisher entities.
    """

    help = "Generates sample publishers."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            dest="count",
            help="Indicates the number of publishers to be created"
        )

    def handle(self, *args, **options):
        """
        Generates up to the given number of sample publishers.
        """

        """Retrieves number of publishers to be created."""
        count = options["count"] or DEFAULT_COUNT

        for _ in range(count):
            """Generates company name."""
            publisher = fake.company()

            """Persist publisher in database."""
            try:
                Publisher.objects.create(name=publisher)
            except IntegrityError:
                """Silently ignore duplicates."""
                pass
