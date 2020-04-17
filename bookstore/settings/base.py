import os

# region Application Definition

INSTALLED_APPS = [

    # region Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # endregion

    # region REST
    "rest_framework",
    "rest_framework.authtoken",
    # endregion

    # region REST Documentation
    "drf_yasg",
    # endregion

    # region Search
    "django_elasticsearch_dsl",
    "django_elasticsearch_dsl_drf",
    # endregion
]

INSTALLED_APPS += [
    "bookstore.account.apps.AccountConfig",
    "bookstore.author.apps.AuthorConfig",
    "bookstore.book.apps.BookConfig",
    "bookstore.docs.apps.DocsConfig",
    "bookstore.publisher.apps.PublisherConfig",
]

# endregion

# region Documentation

SWAGGER_SETTINGS = {

    # Configures to show examples by default.
    "DEFAULT_MODEL_RENDERING": "example",

    # Configures login endpoint so it is possible to authenticate
    # into service from Swagger.
    "LOGIN_URL": "/admin/login/",

    # Configures logout endpoint so it is possible to tear down the
    # session from Swagger.
    "LOGOUT_URL": "/admin/logout/",

    # Points out the bearer token is used to authenticate requests.
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
}

REDOC_SETTINGS = {

    # Moves url to the right panel of the Redoc.
    "PATH_IN_MIDDLE": False
}

# endregion

# region Internationalization

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# endregion

# region Middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# endregion

# region Password Validation

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# endregion

# region Paths

"""Repository files location."""
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

"""Public dir location for http server."""
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")

"""Project files location."""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""Log files location."""
LOGS_DIR = os.path.abspath("/var/log/bookstore/api")

"""Media files location."""
MEDIA_ROOT = os.path.join(PUBLIC_DIR, "media")

"""Create media directory if not exists."""
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

"""Temporary files location."""
TMP_ROOT = os.path.join(ROOT_DIR, "tmp")

"""Create tmp directory if not exists."""
if not os.path.exists(TMP_ROOT):
    os.makedirs(TMP_ROOT)

"""Static files location."""
STATIC_ROOT = os.path.join(TMP_ROOT, "static")
STATICFILES_DIRS = (
    os.path.join(PUBLIC_DIR, "static"),
)

# endregion

# region REST

REST_FRAMEWORK = {

    # Defines date time format.
    "DATETIME_FORMAT": "iso-8601",

    # Defines default authentication method.
    "DEFAULT_AUTHENTICATION_CLASSES": (

        # Django.
        "rest_framework.authentication.SessionAuthentication",
    ),

    # Defines custom exception handler.
    "EXCEPTION_HANDLER": "bookstore.common.exceptions.exception_handler",
}

# endregion

# region Templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# endregion

# region Urls

ROOT_URLCONF = "bookstore.urls"
MEDIA_URL = "/media/"
STATIC_URL = "/static/"

# endregion
