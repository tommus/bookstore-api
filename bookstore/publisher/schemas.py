from drf_yasg.openapi import (
    IN_QUERY,
    Parameter,
    Schema,
    TYPE_STRING, TYPE_OBJECT, TYPE_ARRAY, TYPE_INTEGER, FORMAT_INT64, IN_PATH,
)

"""Used to document publisher detail's path parameters."""
schema_publisher_details_path = [
    Parameter(
        description="A unique integer value identifying given publisher.",
        format=FORMAT_INT64,
        in_=IN_PATH,
        name="id",
        type=TYPE_INTEGER
    )
]

"""Used to document publisher details response."""
schema_publisher_details_response = Schema(
    properties={
        "id": Schema(
            description="A unique integer value identifying given publisher.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "name": Schema(
            description="Publisher's name.",
            type=TYPE_STRING,
        ),
    },
    type=TYPE_OBJECT,
)

"""Used to document publisher list query parameters."""
schema_publisher_list_query = [
    Parameter(
        description="A cursor token that can be used to paginate through the results. "
                    "It can be obtained from `previous` or `next` response body parameters.",
        in_=IN_QUERY,
        name="cursor",
        type=TYPE_STRING,
    ),
]

"""Used to document publisher list response."""
schema_publisher_list_response = Schema(
    properties={
        "previous": Schema(
            description="An optional cursor that points to the previous page "
                        "of publisher list resources.",
            nullable=True,
            type=TYPE_STRING,
        ),
        "next": Schema(
            description="An optional cursor that points to the next page of"
                        "publisher list resources.",
            nullable=True,
            type=TYPE_STRING,
        ),
        "results": Schema(
            description="A page that contains a collection of publishers.",
            items=schema_publisher_details_response,
            type=TYPE_ARRAY,
        ),
    },
    type=TYPE_OBJECT
)
