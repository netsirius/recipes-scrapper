from src.conf.settings import CATEGORIES_CSV_FILE_NAME, BASE_URL, SOURCE, CATEGORIES_URL, logger
import pandas as pd


def get_and_extract_recipe_categories_to_csv(source):
    recipe_categories = []
    category_elements = source.find_all('div', attrs={'class': 'nd-explore-category'})
    for category_element in category_elements:
        category = {}
        category['name'] = category_element.text.strip().lower().replace(" ", "-")
        category['source'] = SOURCE
        category['url'] = '/'.join([BASE_URL, 'recetas', category['name']])
        category['total_recipes'] = 0
        recipe_categories.append(category)
    categories_df = pd.DataFrame(recipe_categories)
    categories_df.to_csv(CATEGORIES_CSV_FILE_NAME)
    return recipe_categories