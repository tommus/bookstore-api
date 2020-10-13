from drf_yasg.openapi import (
    IN_QUERY,
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
            format=FORMAT_INT64,
            type=TYPE_INTEGER,
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

"""Used to document book list query parameters."""
schema_book_list_query = [
    Parameter(
        description="A cursor token that can be used to paginate through the results. "
                    "It can be obtained from `previous` or `next` response body parameters.",
        in_=IN_QUERY,
        name="cursor",
        type=TYPE_STRING,
    ),
]

"""Used to document book list response."""
schema_book_list_response = Schema(
    properties={
        "previous": Schema(
            description="An optional cursor that points to the previous page "
                        "of book list resources.",
            nullable=True,
            type=TYPE_STRING,
        ),
        "next": Schema(
            description="An optional cursor that points to the next page of"
                        "book list resources.",
            nullable=True,
            type=TYPE_STRING,
        ),
        "results": Schema(
            description="A page that contains a collection of books.",
            items=schema_book_list_details_response,
            type=TYPE_ARRAY,
        ),
    },
    type=TYPE_OBJECT
)
