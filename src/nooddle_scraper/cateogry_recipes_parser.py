from src.conf.settings import RECIPES_CSV_FILE_NAME
from src.conf.utils.common import save_to_csv, get_recipes_source_code
from multiprocessing import Pool
import pandas as pd


def extract_recipes_to_csv(categories):
    category_urls = [c['url'] for c in categories]

    thread_pool = Pool(4)
    recipes = []
    for category_page_source, category in thread_pool.map(get_recipes_source_code, category_urls):
        recipe_elements = category_page_source.find_all('div', attrs={'class': 'nd-result'})
        for recipe_element in recipe_elements:
            recipe = extract_recipe(category, recipe_element)
            recipes.append(recipe)
    recipes_df = pd.DataFrame(recipes)
    recipes_df.to_csv(RECIPES_CSV_FILE_NAME)


def extract_recipe(category, recipe_alement):
    recipe = {
        'category': category,
        'name': recipe_alement.find('h2', attrs={'class': 'title'}).text()
    }
    return recipe