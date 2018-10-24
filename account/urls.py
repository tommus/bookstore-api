from django.urls import path

from account.views import RegisterAccountView

# region Application

app_name = "account"

# endregion

# region Patterns

urlpatterns = [
    path("register/", RegisterAccountView.as_view(), name="register")
]

# endregion
