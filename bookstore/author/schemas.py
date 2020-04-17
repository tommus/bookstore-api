from drf_yasg.openapi import (
    IN_QUERY,
    Parameter,
    Schema,
    TYPE_STRING, TYPE_OBJECT, TYPE_ARRAY, TYPE_INTEGER, FORMAT_INT64, IN_PATH,
)

"""Used to document author detail's path parameters."""
schema_author_details_path = [
    Parameter(
        description="A unique integer value identifying given author.",
        format=FORMAT_INT64,
        in_=IN_PATH,
        name="id",
        type=TYPE_INTEGER
    )
]

"""Used to document author details response."""
schema_author_details_response = Schema(
    properties={
        "id": Schema(
            description="A unique integer value identifying given author.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "first_name": Schema(
            description="Author's first name.",
            type=TYPE_STRING,
        ),
        "last_name": Schema(
            description="Author's last name.",
            type=TYPE_STRING,
        )
    },
    type=TYPE_OBJECT,
)

"""Used to document authors list query parameters."""
schema_authors_list_query = [
    Parameter(
        description="A cursor token that can be used to paginate through the results. "
                    "It can be obtained from `previous` or `next` response body parameters.",
        in_=IN_QUERY,
        name="cursor",
        type=TYPE_STRING,
    ),
]

"""Used to document authors list response."""
schema_authors_list_response = Schema(
    properties={
        "previous": Schema(
            description="An optional cursor that points to the previous page "
                        "of author list resources.",
            nullable=True,
            type=TYPE_STRING,
        ),
        "next": Schema(
            description="An optional cursor that points to the next page of"
                        "author list resources.",
            nullable=True,
            type=TYPE_STRING,
        ),
        "results": Schema(
            description="A page that contains a collection of authors.",
            items=schema_author_details_response,
            type=TYPE_ARRAY,
        ),
    },
    type=TYPE_OBJECT
)
