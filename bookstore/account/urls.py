from django.urls import path

from bookstore.account.views import RegisterAccountView, SignInView

app_name = "account"

urlpatterns = [

    # Allows to create an account.
    path(
        route="api/account/register/",
        view=RegisterAccountView.as_view(),
        name="register"
    ),

    # Allows to sign in an account.
    path(
        route="api/account/login/",
        view=SignInView.as_view(),
        name="sign_in"
    ),
]
