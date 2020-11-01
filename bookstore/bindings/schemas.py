from drf_yasg.openapi import (
    Parameter,
    Schema,
    TYPE_STRING, TYPE_OBJECT, TYPE_ARRAY, TYPE_INTEGER, FORMAT_INT64, IN_PATH,
)

"""Used to document binding detail's path parameters."""
schema_binding_details_path = [
    Parameter(
        description="A unique integer value identifying given binding.",
        format=FORMAT_INT64,
        in_=IN_PATH,
        name="id",
        type=TYPE_INTEGER
    )
]

"""Used to document binding details response."""
schema_binding_details_response = Schema(
    properties={
        "id": Schema(
            description="A unique integer value identifying given binding.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "description": Schema(
            description="Binding's description.",
            type=TYPE_STRING,
        ),
    },
    type=TYPE_OBJECT,
)

"""Used to document binding list response."""
schema_binding_list_response = Schema(
    description="A page that contains a collection of bindings.",
    items=schema_binding_details_response,
    type=TYPE_ARRAY
)
