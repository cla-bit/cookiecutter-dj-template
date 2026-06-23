from pathlib import Path

from .env import LOGS_DIR

FORMATTERS = {
    "json": {
        "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
        "format": "%(levelname)s %(asctime)s [%(correlation_id)s] [%(celery_current_id)s] %(name)s - %(message)s",
    },
    "console": {
        "format": "%(levelname)s %(asctime)s [%(correlation_id)s] [%(celery_current_id)s] %(name)s - %(message)s",
    },
}

CONSOLE_HANDLER = {
    "class": "logging.StreamHandler",
    "formatter": "console",
    "filters": ["correlation_id", "celery_tracing"],
}


def file_handler(filename: str | Path = "{{ cookiecutter.project_slug }}.log", level: str = "DEBUG"):
    return {
        "level": level,
        "class": "logging.handlers.TimedRotatingFileHandler",
        "filename": str(LOGS_DIR / filename),  # location of the log files
        "when": "midnight",  # rotate daily at midnight
        "backupCount": 0,  # keep last 7 days of logs
        "formatter": "json",
        "filters": ["correlation_id", "celery_tracing"],
    }
