from rest_framework.routers import DefaultRouter

from bookstore.books.views import BookSearchViewSet

app_name = "books"

router = DefaultRouter()
router.register(
    basename="books",
    prefix="",
    viewset=BookSearchViewSet
)

urlpatterns = router.urls
