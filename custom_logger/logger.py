import logging
from custom_logger.colored_formatter import ColorFormatter

formatter = ColorFormatter("%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s")
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename='server.log')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)
logger.addHandler(file_handler)



