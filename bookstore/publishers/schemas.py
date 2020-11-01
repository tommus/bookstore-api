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
"meta": Schema(
            description="Additional meta information that sheds additional light "
                        "on pagination details.",
            nullable=False,
            properties={
                "limit": Schema(
                    description="Number of results to return per page.",
                    format=FORMAT_INT64,
                    type=TYPE_INTEGER
                ),
                "offset": Schema(
                    description="Additional information about pagination indices.",
                    properties={
                        "current": Schema(
                            description="Index used to retrieve current page.",
                            nullable=False,
                            type=TYPE_INTEGER
                        ),
                        "next": Schema(
                            description="Index to use to retrieve whole next page of items.",
                            nullable=True,
                            type=TYPE_INTEGER
                        ),
                        "previous": Schema(
                            description="Index to use to retrieve whole previous page of items.",
                            nullable=True,
                            type=TYPE_INTEGER
                        )
                    },
                    type=TYPE_OBJECT
                ),
                "size": Schema(
                    description="Number of results returned for given page.",
                    format=FORMAT_INT64,
                    type=TYPE_INTEGER
                ),
                "total": Schema(
                    description="Total number of available author items.",
                    format=FORMAT_INT64,
                    type=TYPE_INTEGER
                )
            },
            type=TYPE_OBJECT
        ),
        "results": Schema(
            description="A page that contains a collection of publishers.",
            items=schema_publisher_details_response,
            type=TYPE_ARRAY,
        ),
    },
    type=TYPE_OBJECT
)
