from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Coloured Custom Logger"
    SERVICE_NAME: str = "coloured_custom_logger"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    _BASE_URL: str = f"https://{HOST}:{PORT}"

    LOG_FILE_DIR: str = "logs"
    LOG_MAX_FILE_SIZE: int = 10  # 10 MB
    LOG_FILE_BACKUP_COUNT: int = 5

    @property
    def log_level(self):
        import logging
        if not self.DEBUG:
            return logging.INFO
        return logging.DEBUG

    @property
    def log_file_name(self):
        return f"{self.SERVICE_NAME}.log"

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "ignore"


@lru_cache(maxsize=1)
def get_settings():
    return Settings()