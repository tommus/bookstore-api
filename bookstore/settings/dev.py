from bookstore.settings.base import *

# region Application Definition

INSTALLED_APPS += [
    "django_extensions",
]

# endregion

# region Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(ROOT_DIR, "db.sqlite3"),
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "bookstore",
#         "USER": "tommus",
#         "PASSWORD": "b0248d59e50ae772a0fd4cc16591fb24",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

# endregion

# region Debug

DEBUG = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", ],
            "propagate": True,
        },
    },
}

# endregion

# region Secret

SECRET_KEY = "bc!!9(w5vs2+5-n%8fd=4b3s^81pxl=d(h%)wkkor)nc-=8)#x"

# endregion

ALLOWED_HOSTS = [
    "*"
]

# region Web Server

WSGI_APPLICATION = "bookstore.wsgi.dev.application"

# endregion
