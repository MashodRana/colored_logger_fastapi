import uvicorn
from fastapi import FastAPI

from custom_logger.logger import CustomLogger
from core.config import get_settings

settings = get_settings()
CustomLogger(
    log_file_name=settings.log_file_name,
    log_file_dir=settings.LOG_FILE_DIR,
    log_level=settings.log_level,
    file_size_max_mb=settings.LOG_MAX_FILE_SIZE,
    file_backup_count=settings.LOG_FILE_BACKUP_COUNT
)

logger = CustomLogger.get_logger(__name__)


app = FastAPI()

logger.info("Before Application Startup")
logger.success('success')
logger.debug('debug')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

@app.get("/")
def root():
    logger.info("Hi I am a colored  logger.......")
    return {"Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
