from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bookstore.author.views import AuthorViewSet, AuthorSearchViewSet

app_name = "author"

router = DefaultRouter()
router.register(
    prefix="authors",
    viewset=AuthorViewSet
)
# router.register(
#     basename="authors_search",
#     prefix="search/authors",
#     viewset=AuthorSearchViewSet
# )

urlpatterns = [

    # Attaches author API urls.
    path(
        route="api/bookstore/",
        view=include(router.urls),
    )
]
