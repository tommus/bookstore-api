from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# region Configuration

admin.site.site_title = "Bookstore API"
admin.site.site_header = "Bookstore API"

# endregion

# region Service Patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/account/", include("account.urls")),
    path("api/bookstore/", include("bookstore.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# endregion
