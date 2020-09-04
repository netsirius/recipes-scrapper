import csv
from selenium import webdriver
from bs4 import BeautifulSoup


def get_category_source_code(page_url):
    driver = webdriver.Chrome()
    driver.get(page_url)
    content = driver.page_source

    soup = BeautifulSoup(content, features="html5lib")
    return soup


def get_recipes_source_code(page_url):
    category_name = page_url.split('/')[2]
    driver = webdriver.Chrome()
    driver.get(page_url)
    content = driver.page_source

    soup = BeautifulSoup(content, features="html5lib")
    return soup, category_name


def save_to_csv(filename, header, rows):
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, header)
        w.writeheader()
        for row in rows:
            w.writerow(row)
