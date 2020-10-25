from rest_framework.routers import DefaultRouter

from bookstore.publishers.views import PublisherViewSet

app_name = "publishers"

router = DefaultRouter()
router.register("", PublisherViewSet)

urlpatterns = router.urls
