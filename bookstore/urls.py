# region Application
from rest_framework.routers import DefaultRouter

from bookstore.views import AuthorViewSet, BindingViewSet, BookViewSet, PublisherViewSet

app_name = "bookstore"

# endregion

# region Patterns

router = DefaultRouter()
router.register("authors", AuthorViewSet, base_name="authors")
router.register("bindings", BindingViewSet, base_name="bindings")
router.register("books", BookViewSet, base_name="books")
router.register("publishers", PublisherViewSet, base_name="publishers")

urlpatterns = []
urlpatterns += router.urls

# endregion
