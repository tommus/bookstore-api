from rest_framework.routers import DefaultRouter

from bookstore.books.views import BookViewSet

app_name = "books"

router = DefaultRouter()
router.register(
    basename="books",
    prefix="",
    viewset=BookViewSet
)

urlpatterns = router.urls
