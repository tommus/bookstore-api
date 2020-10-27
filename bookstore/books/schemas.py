from drf_yasg.openapi import (
    Parameter,
    Schema,
    TYPE_BOOLEAN,
    TYPE_STRING,
    TYPE_OBJECT,
    TYPE_ARRAY,
    TYPE_INTEGER,
    FORMAT_INT64,
    IN_PATH,
    TYPE_NUMBER,
)

"""Used to document book detail's path parameters."""
schema_book_details_path = [
    Parameter(
        description="A unique integer value identifying given book.",
        format=FORMAT_INT64,
        in_=IN_PATH,
        name="id",
        type=TYPE_INTEGER
    )
]

"""Used to document book details response returned in a pageable list."""
schema_book_list_details_response = Schema(
    properties={
        "id": Schema(
            description="A unique integer value identifying given book.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "title": Schema(
            description="Book's title.",
            type=TYPE_STRING,
        ),
        "author": Schema(
            description="Book's author id.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "publisher": Schema(
            description="Books's publisher id.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "publication_year": Schema(
            description="Book's publication year.",
            type=TYPE_INTEGER,
        ),
        "cover": Schema(
            description="Book's cover type.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
    },
    type=TYPE_OBJECT,
)

"""Used to document book details response."""
schema_book_details_response = Schema(
    properties={
        "id": Schema(
            description="A unique integer value identifying given book.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "title": Schema(
            description="Book's title.",
            type=TYPE_STRING,
        ),
        "author": Schema(
            description="Book's author id.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "publisher": Schema(
            description="Books's publisher id.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "publication_year": Schema(
            description="Book's publication year.",
            type=TYPE_INTEGER,
        ),
        "cover": Schema(
            description="Book's cover type.",
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
        ),
        "format": Schema(
            description="Book's format.",
            type=TYPE_STRING,
        ),
        "isbn": Schema(
            description="Book's ISBN.",
            type=TYPE_STRING,
        ),
        "ean": Schema(
            description="Book's EAN.",
            type=TYPE_STRING,
        ),
        "release_date": Schema(
            description="Book's release date.",
            type=TYPE_STRING,
        ),
        "available": Schema(
            description="An information whether given book is available for sell.",
            type=TYPE_BOOLEAN,
        ),
        "price_base": Schema(
            description="Book's price.",
            type=TYPE_NUMBER,
        ),
        "price_discounted": Schema(
            description="Book's discounted price.",
            type=TYPE_NUMBER,
        ),
        "description": Schema(
            description="Book's description.",
            type=TYPE_STRING,
        )
    },
    type=TYPE_OBJECT,
)

"""Used to document book list response."""
schema_book_list_response = Schema(
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
            description="A page that contains a collection of books.",
            items=schema_book_list_details_response,
            type=TYPE_ARRAY,
        ),
    },
    type=TYPE_OBJECT
)
