"""
Wiki scraper to download hero thumbnail, 2D model, and ability icons from "deadlocked.wiki".
"""

import requests
from bs4 import BeautifulSoup

from config import WIKI_BASE_URL
from utils import get_hero_dir, highres_url, download

heroes_page = requests.get(WIKI_BASE_URL + "/heroes")
heroes_soup = BeautifulSoup(heroes_page.content, "html.parser")

# Find all tables (each table is a hero card)
tables = heroes_soup.find_all('table')

for table in tables:
    imgs = table.find_all('img')

    # First image is the hero model
    img = imgs.pop(0)

    # Get the hero name, page, and directory path for the hero
    hero_name = img.parent['title'].lower()
    hero_page = img.parent['href']
    hero_dir = get_hero_dir(hero_name)

    # Download the hero model
    model_url = highres_url(img['srcset'])
    file_ext = model_url.rpartition('.')[-1]
    model_path = hero_dir / "assets" / f"hero_model.{file_ext}"
    download(WIKI_BASE_URL + model_url, model_path)

    # Filter out background images (e.g. Passive_ability_frame.png)
    imgs = [img for img in imgs if 'frame' not in img['src']]

    # Download ability icons
    for img in imgs:
        img_url = highres_url(img['srcset'])

        file_name = img_url.lower().rpartition('/')[-1]
        # Replace 'XXXpx-' with 'ability_' prefix
        file_name = 'ability_' + file_name.partition('-')[-1]

        icon_path = hero_dir / "assets" / file_name
        download(WIKI_BASE_URL + img_url, icon_path)

    # Visit the hero page
    hero_page = requests.get(WIKI_BASE_URL + hero_page)
    hero_soup = BeautifulSoup(hero_page.content, "html.parser")

    # Find table 'wikitable infobox' which contains the hero thumbnail
    infobox = hero_soup.find('table', class_='wikitable infobox')
    img = infobox.find('img')
    img_url = highres_url(img['srcset'])

    # Download the thumbnail
    thumbnail_path = hero_dir / "assets" / "hero_thumbnail.png"
    download(WIKI_BASE_URL + img_url, thumbnail_path)
