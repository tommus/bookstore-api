from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = "docs"

schema_view = get_schema_view(
    info=openapi.Info(
        title="Bookstore API",
        default_version="v1",
        description="Playground sandbox API.",
        contact=openapi.Contact(email="tomasz.dzieniak@windly.co"),
        license=openapi.License(name="Apache-2.0"),
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

urlpatterns = [

    # Attaches docs API urls.
    path(
        route="docs/redoc",
        view=schema_view.with_ui("redoc", cache_timeout=0)
    ),

    # Attaches swagger API urls.
    path(
        route="docs/swagger",
        view=schema_view.with_ui("swagger", cache_timeout=0)
    ),
]
