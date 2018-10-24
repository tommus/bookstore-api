from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# region Service Patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/account/", include("account.urls", namespace="api")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# endregion
