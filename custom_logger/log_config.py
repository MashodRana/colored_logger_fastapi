import logging

from core.config import get_settings
from custom_logger.custom_formatters import ConsoleFormatter, FileFormatter

# Console handler with color
console_handler = {
    "class": "logging.StreamHandler",
    "formatter": "colored",
    # "stream": "ext://sys.stdout",
    "level": "DEBUG"
}

# File handler
file_handler = {
    "class": "logging.handlers.RotatingFileHandler",
    "formatter": "file_formatter",
    "filename": "app.log",
    "maxBytes": 5 * 1024 * 1024,
    "backupCount": 3,
    "level": "INFO",
    "encoding": "utf-8"
}

LOG_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s | %(name)s | %(filename)s | %(classname)s | %(funcName)s | line:%(lineno)d | %(message)s"
            },
            "colored": {
                "()": ConsoleFormatter,
                "format": "%(asctime)s | %(name)s | %(filename)s | %(classname)s | %(funcName)s | line:%(lineno)d | %(message)s"
            },
            "file_formatter": {
                "()": FileFormatter,
                "format": "%(asctime)s | %(name)s | %(filename)s | %(classname)s | %(funcName)s | line:%(lineno)d | %(message)s"
            }
        },
        "handlers": {
            "console": console_handler,
            "file": file_handler,
        },
        "loggers": {
            "uvicorn": {"handlers": ["console", "file"], "level": "INFO", "propagate": False},
            "uvicorn.error": {"handlers": ["console", "file"], "level": "INFO", "propagate": False},
            "uvicorn.access": {"handlers": ["console", "file"], "level": "INFO", "propagate": False},
            "my_fastapi_logger": {"handlers": ["console", "file"], "level": "DEBUG", "propagate": False},
        },
    }