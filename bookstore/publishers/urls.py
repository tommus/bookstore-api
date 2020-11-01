from rest_framework.routers import DefaultRouter

from bookstore.publishers.views import PublisherViewSet

app_name = "publishers"

router = DefaultRouter()
router.register(
    basename="publishers",
    prefix="",
    viewset=PublisherViewSet
)

urlpatterns = router.urls
