import os
import logging

CONF_PATH = os.path.abspath(__file__)

logger = None


def configure_logger():
    global logger
    if not logger:
        FORMAT = '%(asctime)s - %(name)s - (%(levelname)s): %(message)s'
        logging.basicConfig(datefmt='%y/%m/%d %H:%M:%S', format=FORMAT)
        logger = logging.getLogger('recipes-scrapper')
        logger.setLevel(logging.INFO)

    return logger


logger = configure_logger()

SOURCE = 'nooddle'
BASE_URL = "https://www.nooddle.es"

CATEGORIES_URL = BASE_URL + '/explore'
CATEGORIES_CSV_FILE_NAME = f'../output/{SOURCE}_recipe_categories.csv'

RECIPES_CSV_FILE_NAME = f'../output/{SOURCE}_recipes.csv'
