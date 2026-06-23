from .base import CONSOLE_HANDLER, FORMATTERS, file_handler
from .env import DJANGO_ENV


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": FORMATTERS,
    "filters": {
        "correlation_id": {"()": "django_guid.log_filters.CorrelationId"},
        "celery_tracing": {"()": "django_guid.integrations.celery.log_filters.CeleryTracing"},
    },
    "handlers": {
        "console": CONSOLE_HANDLER,
        # APP LOGS
        "file": file_handler(filename=f"{DJANGO_ENV}.log", level="INFO"),
        # ACCESS & SECURITY SYSTEM LOGS
        "file.access": file_handler("access.log", "INFO"),
        "file.security": file_handler("security.log", "WARNING"),
        # CELERY LOGS
        "file.celery": file_handler(filename="celery.log", level="INFO"),
        # APPLICATION LOGS
    },
    "loggers": {
        "root": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "access": {
            "handlers": ["console", "file.access"],
            "level": "INFO",
            "propagate": False,
        },
        "security": {
            "handlers": ["console", "file.security"],
            "level": "WARNING",
            "propagate": False,
        },
        "celery": {
            "handlers": ["console", "file.celery"],
            "level": "INFO",
            "propagate": False,
        },
        "celery.task": {
            "handlers": ["console", "file.celery"],
            "level": "INFO",
            "propagate": False,
        },
        # ADD YOUR LOG FILES
    },
}
