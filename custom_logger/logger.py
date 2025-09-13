from typing import Any
from pathlib import Path
from threading import Lock
import logging
from logging.handlers import RotatingFileHandler

from custom_logger.custom_formatters import FileFormatter, ConsoleFormatter


class CustomLogger:
    _instance = None
    _lock = Lock()
    _is_configured = False

    SUCCESS_LEVEL_NUM = 25  # Between INFO(20) and WARNING(30)

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(CustomLogger, cls).__new__(cls)
        return cls._instance

    def __init__(
            self,
            log_file_name: str,
            log_file_dir: str,
            log_level: int,
            file_size_max_mb: int,
            file_backup_count: int
    ):
        if CustomLogger._is_configured:
            return

        log_dir = Path(log_file_dir)
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir.joinpath(log_file_name)

        # Root logger config
        root_logger = logging.getLogger()
        root_logger.setLevel(log_level)

        console_handler = logging.StreamHandler()
        file_handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=file_size_max_mb * 1024 * 1024,
            backupCount=file_backup_count,
            encoding='utf-8'
        )
        log_format = "%(asctime)s | %(module)s | %(funcName)s | line:%(lineno)d | %(levelname)s | %(message)s"
        file_handler.setFormatter(FileFormatter(log_format))
        console_handler.setFormatter(ConsoleFormatter(log_format))

        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)

        # Setup SUCCESS level inside the class
        self.__setup_success_level()
        # logging.SUCCESS = CustomLogger.SUCCESS_LEVEL_NUM

        CustomLogger._is_configured = True

    @classmethod
    def __setup_success_level(cls):
        # Add custom SUCCESS level
        logging.addLevelName(cls.SUCCESS_LEVEL_NUM, "SUCCESS")

        def success(self_logger, message, *args, **kwargs):
            if self_logger.isEnabledFor(cls.SUCCESS_LEVEL_NUM):
                self_logger._log(cls.SUCCESS_LEVEL_NUM, message, args, **kwargs)
        logging.Logger.success = success

    @classmethod
    def get_logger(cls, name: str) -> Any:
        """Get a logger named after the module (e.g., __name__)"""
        return logging.getLogger(name if name else __name__)
