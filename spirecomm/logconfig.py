import logging as l
import time
from datetime import datetime
import os

DEBUG_LOGGER_NAME = "debug_logger"
DATA_SCRAPER_NAME = "scrape_logger"

# Code from https://stackoverflow.com/a/11233293
def setup_logger(name, log_file, level=l.INFO):
    """To setup as many loggers as you want"""
    formatter = l.Formatter('%(levelname)s,%(message)s')

    handler = l.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = l.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

current_milli_time = lambda: int(round(time.time() * 1000))

class CustomLogger():
    """A thin wrap around the logging module because I want timestamps in nanoseconds and apparently strftime can't do that."""
    def __init__(self, logger):
        self.logger = logger

    def info(self, message):
        self.logger.info(f"{current_milli_time()},{message}")

    def debug(self, message):
        self.logger.debug(f"{current_milli_time()},{message}")

    def info(self, message):
        self.logger.info(f"{current_milli_time()},{message}")

    def warning(self, message):
        self.logger.warning(f"{current_milli_time()},{message}")

    def error(self, message):
        self.logger.error(f"{current_milli_time()},{message}")


# these are meant for importing by other classes
now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")

DEBUG_PATH = f"logs/debug/{timestamp}_spirecomm.debug.log"
SCRAPE_PATH =f"logs/scrape/{timestamp}_spirecomm.scrape.csv"

DEBUG_FOLDERS = "/".join(DEBUG_PATH.split("/")[:-1])
SCRAPE_FOLDERS =  "/".join(SCRAPE_PATH.split("/")[:-1])

if not os.path.exists(DEBUG_FOLDERS):
    os.makedirs(DEBUG_FOLDERS)

if not os.path.exists(SCRAPE_FOLDERS):
    os.makedirs(SCRAPE_FOLDERS)


debug_logger = CustomLogger(setup_logger(DEBUG_LOGGER_NAME, DEBUG_PATH, l.DEBUG))
scrape_logger = CustomLogger(setup_logger(DATA_SCRAPER_NAME, SCRAPE_PATH, l.DEBUG))
