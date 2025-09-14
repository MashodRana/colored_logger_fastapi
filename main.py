import uvicorn
from fastapi import FastAPI
import logging
from custom_logger.logger import CustomLogger
from core.config import get_settings
from custom_logger.log_config import LOG_CONFIG

settings = get_settings()
logging.config.dictConfig(LOG_CONFIG)

app = FastAPI()
logger = logging.getLogger("my_fastapi_logger")

logger.info("Before Application Startup")
# logger.success('success')
logger.debug('debug')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

@app.get("/")
def root():
    logger.info("Hi I am a colored  logger.......")
    return {"Hello World"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=80)
