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

# endregion

# region Debug

DEBUG = False

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "debug.log"),
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "propagate": True,
        },
    },
}

# endregion

# region Secret

SECRET_KEY = "bc!!9(w5vs2+5-n%8fd=4b3s^81pxl=d(h%)wkkor)nc-=8)#x"

# endregion

ALLOWED_HOSTS = [
    "bookstore.windly.co"
]

# region Web Server

WSGI_APPLICATION = "bookstore.wsgi.prod.application"

# endregion
