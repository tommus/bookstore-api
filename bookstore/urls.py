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

    # Attaches accounts API urls.
    path(
        route="api/v1/accounts/",
        view=include("bookstore.accounts.urls", namespace="v1")
    ),

    # Attaches authors API urls.
    path(
        route="api/v1/authors/",
        view=include("bookstore.authors.urls", namespace="v1")
    ),

    # Attaches bindings API urls.
    path(
        route="api/v1/bindings/",
        view=include("bookstore.bindings.urls", namespace="v1")
    ),

    # Attaches books API urls.
    path(
        route="api/v1/books/",
        view=include("bookstore.books.urls", namespace="v1")
    ),

    # Attaches docs API urls.
    path(
        route="api/v1/docs/",
        view=include("bookstore.docs.urls.docs", namespace="v1")
    ),

    # Attaches playground API urls.
    path(
        route="api/v1/playground/",
        view=include("bookstore.docs.urls.playground", namespace="v1")
    ),

    # Attaches publishers API urls.
    path(
        route="api/v1/publishers/",
        view=include("bookstore.publishers.urls", namespace="v1")
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
