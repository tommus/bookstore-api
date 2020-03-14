from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bookstore.publisher.views import PublisherViewSet

app_name = "publisher"

router = DefaultRouter()
router.register("publishers", PublisherViewSet)

urlpatterns = [

    # Attaches publisher API urls.
    path(
        route="api/bookstore/",
        view=include(router.urls),
    )
]
