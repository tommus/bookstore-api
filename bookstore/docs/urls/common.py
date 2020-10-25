from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

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
