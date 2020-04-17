from drf_yasg.openapi import (
    FORMAT_EMAIL,
    FORMAT_PASSWORD,
    Schema,
    TYPE_ARRAY,
    TYPE_OBJECT,
    TYPE_STRING,
)

"""Used to document register account request."""
schema_register_request = Schema(
    properties={
        "email": Schema(
            description="Email address that will be associated with account.",
            format=FORMAT_EMAIL,
            type=TYPE_STRING,
        ),
        "username": Schema(
            description="Username that will be associated with account.",
            type=TYPE_STRING,
        ),
        "password": Schema(
            description="Password that should be used during authentication.",
            format=FORMAT_PASSWORD,
            type=TYPE_STRING
        ),
        "first_name": Schema(
            description="User's first name.",
            type=TYPE_STRING,
        ),
        "last_name": Schema(
            description="User's last name.",
            type=TYPE_STRING,
        ),
    },
    required=["email", "username", "password", ],
    type=TYPE_OBJECT,
)

"""Used to document register account response."""
schema_register_response = Schema(
    properties={
        "email": Schema(
            description="Email address associated with the account.",
            format=FORMAT_EMAIL,
            type=TYPE_STRING,
        ),
        "username": Schema(
            description="Username that should be used to authenticate user.",
            type=TYPE_STRING,
        ),
        "first_name": Schema(
            description="User's first name.",
            type=TYPE_STRING,
        ),
        "last_name": Schema(
            description="User's last name.",
            type=TYPE_STRING,
        ),
    },
    type=TYPE_OBJECT,
)

"""Used to document register validation errors."""
schema_register_validation_error = Schema(
    properties={
        "email": Schema(
            description="Email-related validation error messages.",
            items=Schema(type=TYPE_STRING),
            type=TYPE_ARRAY,
        ),
        "username": Schema(
            description="Username-related validation error messages.",
            items=Schema(type=TYPE_STRING),
            type=TYPE_ARRAY,
        ),
        "password": Schema(
            description="Password-related validation error messages.",
            items=Schema(type=TYPE_STRING),
            type=TYPE_ARRAY,
        ),
        "first_name": Schema(
            description="First name-related validation error messages.",
            items=Schema(type=TYPE_STRING),
            type=TYPE_ARRAY,
        ),
        "last_name": Schema(
            description="Last name-related validation error messages.",
            items=Schema(type=TYPE_STRING),
            type=TYPE_ARRAY,
        ),
    },
    type=TYPE_OBJECT
)

"""Used to document token request."""
schema_login_request = Schema(
    properties={
        "username": Schema(
            description="Username that should be used during authentication.",
            format=FORMAT_EMAIL,
            type=TYPE_STRING,
        ),
        "password": Schema(
            description="Password that should be used during authentication.",
            format=FORMAT_PASSWORD,
            type=TYPE_STRING
        ),
    },
    required=["username", "password", ],
    type=TYPE_OBJECT,
)

"""Used to document convert token response."""
schema_login_response = Schema(
    properties={
        "access_token": Schema(
            description="In-app access token that should be used in "
                        "further requests.",
            type=TYPE_STRING,
        ),
    },
    type=TYPE_OBJECT
)
