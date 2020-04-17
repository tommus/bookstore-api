from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bookstore.book.views.bindings import BindingViewSet
from bookstore.book.views.books import BookViewSet

app_name = "book"

router = DefaultRouter()
router.register("bindings", BindingViewSet)
router.register("books", BookViewSet)

urlpatterns = [

    # Attaches book API urls.
    path(
        route="api/bookstore/",
        view=include(router.urls),
    )
]
