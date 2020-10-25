from bookstore.books.views import BookViewSet
from rest_framework.routers import DefaultRouter

app_name = "books"

router = DefaultRouter()
router.register("", BookViewSet)

urlpatterns = router.urls
