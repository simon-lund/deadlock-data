from pathlib import Path

import requests

from config import HERO_MAP, HEROES_DIR


def get_hero_dir(hero_name: str) -> Path:
    """
    Returns the directory path for the hero.
    """
    for hero in HERO_MAP:
        names = [hero['name'], *hero['old_names']]
        names = list(map(str.lower, names))

        if hero_name.lower() in names:
            return HEROES_DIR / hero['id']

    raise KeyError(f"Hero {hero_name} not found.")


def highres_url(srcset: str) -> str:
    """
    Get the highest resolution image URL from the srcset attribute.
    """
    return srcset.split(' ')[-2]


def download(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as f:
        f.write(response.content)
