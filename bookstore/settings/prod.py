from bookstore.settings.base import *

# region Application Definition

INSTALLED_APPS += [
    "django_extensions",
]

# endregion

# region Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bookstore",
        "USER": "tommus",
        "PASSWORD": "b0248d59e50ae772a0fd4cc16591fb24",
        "HOST": "localhost",
        "PORT": "5432",
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
            "class": "logging.StreamHandler",
            "level": "DEBUG",
        },
        "rotating": {
            "backupCount": 14,
            "maxBytes": 1024 * 1024 * 10,
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(LOGS_DIR, "debug.log"),
            "level": "DEBUG",
            "when": "midnight",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console", "rotating"],
            "propagate": True,
        },
    },
}

# endregion

# region Search

ELASTICSEARCH_DSL = {
    "default": {
        "hosts": "localhost:9200"
    }
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
