"""
Downloads 2D hero models from "deadlocked.wiki/heroes".
"""

import requests
from bs4 import BeautifulSoup

from config import WIKI_BASE_URL
from utils import get_hero_dir


def main():
    page = requests.get(WIKI_BASE_URL + "/heroes")
    soup = BeautifulSoup(page.content, "html.parser")

    # Find all tables (each table is a hero card)
    tables = soup.find_all('table')

    for table in tables:
        # First image is the hero model
        img = table.find('img')
        img_url: str = img['src']

        # img.parent.title is the hero name
        hero_name = img.parent['title'].lower()

        # Download the model
        hero_dir = get_hero_dir(hero_name)
        file_ext = img_url.rpartition('.')[-1]
        model_path = hero_dir / "assets" / f"model.{file_ext}"
        with open(model_path, 'wb') as f:
            response = requests.get(WIKI_BASE_URL + img_url)
            response.raise_for_status()
            f.write(response.content)


if __name__ == '__main__':
    main()