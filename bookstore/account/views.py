from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_200_OK, HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from bookstore.account.exceptions import InvalidCredentials
from bookstore.account.schemas import (
    schema_register_request,
    schema_register_response,
    schema_register_validation_error,
    schema_login_request,
    schema_login_response,
)
from bookstore.account.serializers import AccountSerializer
from bookstore.common.schemas import schema_error


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_id="account:register",
        operation_summary="Create account",
        operation_description="Allows to create account in the system.",
        request_body=schema_register_request,
        responses={
            HTTP_201_CREATED: openapi.Response(
                description="Account has been created.",
                schema=schema_register_response,
            ),
            HTTP_422_UNPROCESSABLE_ENTITY: openapi.Response(
                description="An error occurred while validating request.",
                schema=schema_register_validation_error,
            ),
        },
        tags=["account"],
    )
)
class RegisterAccountView(generics.CreateAPIView):
    """Creates account."""

    authentication_classes = ()
    permission_classes = ()
    serializer_class = AccountSerializer


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_id="account:login",
        operation_summary="Sign in user",
        operation_description="Allows to sign user into service.",
        request_body=schema_login_request,
        responses={
            HTTP_200_OK: openapi.Response(
                description="Sign in success.",
                schema=schema_login_response,
            ),
            HTTP_400_BAD_REQUEST: openapi.Response(
                description="Request failed.",
                schema=schema_error("invalid_credentials"),
            ),
        },
        tags=["account"],
    )
)
class SignInView(APIView):
    """Signs in a user."""

    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            return Response(
                data={"access_token": user.auth_token.key},
                status=status.HTTP_200_OK
            )
        else:
            raise InvalidCredentials()
