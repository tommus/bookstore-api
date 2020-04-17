from drf_yasg.openapi import (
    Schema,
    TYPE_OBJECT,
    TYPE_STRING,
)


def schema_error(*errors: str):
    """Used to document error response of various types."""

    return Schema(
        properties={
            "error": Schema(
                description="A key that identifies given error.",
                enum=[*errors],
                type=TYPE_STRING,
            ),
            "error_description": Schema(
                description="Human-readable error description. Does not support translation.",
                type=TYPE_STRING,
            ),
        },
        type=TYPE_OBJECT
    )
