from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bookstore.author.views import AuthorViewSet

app_name = "author"

router = DefaultRouter()
router.register("authors", AuthorViewSet)

urlpatterns = [

    # Attaches author API urls.
    path(
        route="api/bookstore/",
        view=include(router.urls),
    )
]
