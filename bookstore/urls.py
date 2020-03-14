from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [

    # Enables admin panel and APIs.
    path(
        route="admin/",
        view=admin.site.urls
    ),

    # Attaches account API urls.
    path(
        route="",
        view=include("bookstore.account.urls", namespace="account")
    ),

    # Attaches author API urls.
    path(
        route="",
        view=include("bookstore.author.urls", namespace="author")
    ),

    # Attaches book API urls.
    path(
        route="",
        view=include("bookstore.book.urls", namespace="book")
    ),

    # Attaches docs API urls.
    path(
        route="",
        view=include("bookstore.docs.urls", namespace="docs")
    ),

    # Attaches publisher API urls.
    path(
        route="",
        view=include("bookstore.publisher.urls", namespace="publisher")
    ),
]


def mediafiles_urlpatterns(prefix=None):
    """Helper function to return a URL pattern for serving media files."""

    # Load prefix from settings if not provided.
    if prefix is None:
        prefix = settings.MEDIA_URL

    # Create url pattern for media files.
    return static(prefix, document_root=settings.MEDIA_ROOT)


urlpatterns += mediafiles_urlpatterns()
urlpatterns += staticfiles_urlpatterns()

admin.site.site_title = "Bookstore API"
admin.site.site_header = "Bookstore API"
