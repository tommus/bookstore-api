from rest_framework.routers import DefaultRouter

from bookstore.bindings.views import BindingViewSet

app_name = "books"

router = DefaultRouter()
router.register("", BindingViewSet)

urlpatterns = router.urls
