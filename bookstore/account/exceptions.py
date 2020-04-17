from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidCredentials(APIException):
    """An exception that should be raised in case if incorrect
    credentials has been used."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "invalid_credentials"
    default_detail = _("Incorrect authentication credentials.")
