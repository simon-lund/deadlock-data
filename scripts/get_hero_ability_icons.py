"""
Downloads icons for all hero abilities from "deadlocked.wiki/heroes".
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
        # Find all images in the table
        imgs = table.find_all('img')

        # Skip the first image (hero model) and get the hero name
        hero_name = imgs.pop(0).parent['title'].lower()
        hero_dir = get_hero_dir(hero_name)

        # Remove background images with name:
        # '/images/thumb/8/8a/Passive_ability_frame.png/69px-Passive_ability_frame.png'
        imgs = [img for img in imgs if 'frame' not in img['src']]


        # Download the icons
        for img in imgs:
            img_url: str = img['src']
            response = requests.get(WIKI_BASE_URL + img_url)
            response.raise_for_status()

            # Format file name and replace '48px-' with 'ability-' prefix
            file_name = img_url.lower().rpartition('/')[-1]
            file_name = file_name.replace('48px-', 'ability-')

            icon_path = hero_dir / "assets" / file_name
            with open(icon_path, 'wb') as f:
                f.write(response.content)


if __name__ == '__main__':
    main()