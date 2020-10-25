from rest_framework.routers import DefaultRouter

from bookstore.authors.views import AuthorViewSet

app_name = "authors"

router = DefaultRouter()
router.register(
    prefix="",
    viewset=AuthorViewSet
)

urlpatterns = router.urls
