from django.urls import path

from bookstore.docs.urls.common import schema_view

app_name = "docs"

urlpatterns = [

    # Attaches swagger API urls.
    path(
        route="",
        view=schema_view.with_ui("swagger", cache_timeout=0)
    )
]
