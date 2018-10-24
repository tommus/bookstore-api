from django.urls import path

from account.views import RegisterAccountView, SignInView

# region Application

app_name = "account"

# endregion

# region Patterns

urlpatterns = [
    path("register/", RegisterAccountView.as_view(), name="register"),
    path("login/", SignInView.as_view(), name="sign_in"),
]

# endregion
