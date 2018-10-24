from rest_framework import generics

from account.serializers import AccountSerializer


# region Account Registration

class RegisterAccountView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AccountSerializer

# endregion
