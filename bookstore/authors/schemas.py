from drf_yasg.openapi import (
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
            type=TYPE_INTEGER
        ),
        "first_name": Schema(
            description="Author's first name.",
            type=TYPE_STRING
        ),
        "last_name": Schema(
            description="Author's last name.",
            type=TYPE_STRING
        )
    },
    type=TYPE_OBJECT
)

"""Used to document author list response."""
schema_author_list_response = Schema(
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
                    description="Additional information about pagination indexes",
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
            description="A page that contains a collection of authors.",
            items=schema_author_details_response,
            type=TYPE_ARRAY
        )
    },
    type=TYPE_OBJECT
)
