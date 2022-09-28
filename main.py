import logging

import uvicorn
from fastapi import FastAPI

from custom_logger.logger import logger


app = FastAPI()

logger.info("Before Application Startup")

# Adding Custom Level: success level
logging.SUCCESS = 25  # between WARNING and INFO
logging.addLevelName(logging.SUCCESS, 'SUCCESS')
setattr(logger, 'success', lambda message, *args: logger._log(logging.SUCCESS, message, args))

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
