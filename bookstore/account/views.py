from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from bookstore.account.serializers import AccountSerializer


class RegisterAccountView(generics.CreateAPIView):
    """
    Creates account.
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = AccountSerializer


class SignInView(APIView):
    """
    Signs in a user.
    """

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
            return Response(
                data={"error": "Cannot authenticate with given credentials."},
                status=status.HTTP_401_UNAUTHORIZED
            )