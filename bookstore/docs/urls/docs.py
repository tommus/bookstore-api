from django.urls import path

from docs.urls.common import schema_view

app_name = "docs"

urlpatterns = [

    # Attaches docs API urls.
    path(
        route="",
        view=schema_view.with_ui("redoc", cache_timeout=0)
    )
]
