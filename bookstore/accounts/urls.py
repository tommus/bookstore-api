from django.urls import path

from bookstore.accounts.views import RegisterAccountView, SignInView

app_name = "accounts"

urlpatterns = [

    # Allows to create an account.
    path(
        route="register/",
        view=RegisterAccountView.as_view(),
        name="register"
    ),

    # Allows to sign in an account.
    path(
        route="login/",
        view=SignInView.as_view(),
        name="login"
    ),
]
