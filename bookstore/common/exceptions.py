from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import set_rollback


# noinspection PyUnresolvedReferences
def exception_handler(exc, _=None):
    """Exception handle that propagates exceptions in consistent
    format."""

    # Handle bad request error.
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    # Handle permission denied error.
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    # Handle API errors.
    if isinstance(exc, exceptions.APIException):

        # Prepare headers.
        headers = {}

        # Append WWW-Authenticate header if available.
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header

        # Append Retry-After header if available.
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

        # For validation error, propagate data as is but change status code.
        if isinstance(exc, ValidationError):
            data = exc.detail
            exc.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

        # For other errors, format data accordingly.
        else:
            data = {
                "error": exc.default_code,
                "error_description": exc.default_detail
            }

        # Rollback atomic connections.
        set_rollback()

        # Return response with headers.
        return Response(
            data=data,
            status=exc.status_code,
            headers=headers
        )

    # Fallback to no response for unknown error type.
    return None
