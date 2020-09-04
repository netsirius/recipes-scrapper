from src.conf.settings import CATEGORIES_URL, CATEGORIES_CSV_FILE_NAME
from src.conf.utils.common import get_category_source_code, save_to_csv
from src.nooddle_scraper.categories_parser import get_and_extract_recipe_categories_to_csv
from src.nooddle_scraper.cateogry_recipes_parser import extract_recipes_to_csv

if __name__ == '__main__':
    # Scrapping nooddle categories
    source = get_category_source_code(CATEGORIES_URL)
    categories = get_and_extract_recipe_categories_to_csv(source)

    # Scrapping nooddle recipes
    extract_recipes_to_csv(categories)
