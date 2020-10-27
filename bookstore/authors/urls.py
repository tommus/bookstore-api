from rest_framework.routers import DefaultRouter

from bookstore.authors.views import AuthorSearchViewSet

app_name = "authors"

router = DefaultRouter()
router.register(
    basename="authors",
    prefix="",
    viewset=AuthorSearchViewSet
)

urlpatterns = router.urls
