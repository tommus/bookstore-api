from django.core.management import BaseCommand
from faker import Factory
from faker.providers import person

from bookstore.authors.models import Author

DEFAULT_COUNT = 25

fake = Factory.create()
fake.add_provider(person)


class Command(BaseCommand):
    """
    Implements Django management command and allows to generate sample author entities.
    """
    help = "Generates sample authors."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            dest="count",
            help="Indicates the number of publishers to be created"
        )

    def handle(self, *args, **options):
        """
        Generates up to the given number of sample authors.
        """

        """Retrieves number of authors to be created."""
        count = options["count"] or DEFAULT_COUNT

        for _ in range(count):
            """Generates author first and last name."""
            first_name = fake.first_name()
            last_name = fake.last_name()

            """Persists author in database."""
            Author.objects.create(first_name=first_name, last_name=last_name)
