from random import randint

from django.core.management import BaseCommand
from faker import Factory
from faker.providers import company, lorem, date_time, isbn, color

from bookstore.author.models import Author
from bookstore.book.models import Binding, Book
from bookstore.publisher.models import Publisher

DEFAULT_COUNT = 100

fake = Factory.create()
fake.add_provider(color)
fake.add_provider(company)
fake.add_provider(date_time)
fake.add_provider(isbn)
fake.add_provider(lorem)


class Command(BaseCommand):
    """
    Implements Django management command and allows to generate sample bookstore entities.
    """

    help = "Generates sample books."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            dest="count",
            help="Indicates the number of entities to be created"
        )

    def handle(self, *args, **options):
        """
        Generates up to the given number of sample books.
        """

        """Retrieves number of books to be created."""
        count = options["count"] or DEFAULT_COUNT

        for _ in range(count):
            """Generate book title."""
            title = fake.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None)[:-1]

            """Pick random author."""
            author = Author.objects.order_by("?").first()

            """Pick random publisher."""
            publisher = Publisher.objects.order_by("?").first()

            """Generate publication year."""
            publication_year = fake.year()

            """Pick random binding."""
            binding = Binding.objects.order_by("?").first()

            """Generate number of pages."""
            pages = randint(100, 3000)

            """Generate random format."""
            format = "{0}.{1} x {2}.{3} cm".format(
                randint(10, 30),
                randint(0, 9),
                randint(10, 30),
                randint(0, 9)
            )

            """Generate random isbn."""
            isbn = fake.isbn13(separator="-")

            """Generate random ean."""
            ean = randint(1000000000000, 9999999999999)

            """Generate release date."""
            release_date = fake.date_this_century(before_today=True, after_today=False)

            """Generate stock count."""
            available = randint(0, 1000)

            """Generate price base."""
            price_base = randint(1000, 30000) / 100

            """Generate price discounted."""
            price_discounted = price_base * (randint(0, 35) / 100)

            """Generate description."""
            description_raw = fake.paragraphs(nb=4, ext_word_list=None)
            description = " ".join(description_raw)

            """Generate image."""
            image = "https://via.placeholder.com/455x725/{0}.png".format(
                fake.hex_color()[1:]
            )

            """Persist book in database."""
            Book.objects.create(
                title=title,
                author=author,
                publisher=publisher,
                publication_year=publication_year,
                binding=binding,
                pages=pages,
                format=format,
                isbn=isbn,
                ean=ean,
                release_date=release_date,
                available=available,
                price_base=price_base,
                price_discounted=price_discounted,
                description=description,
                cover=None,
                cover_url=image
            )
