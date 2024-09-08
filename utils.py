from pathlib import Path

from config import HERO_MAP, HEROES_DIR


def get_hero_dir(hero_name: str) -> Path:
    """
    Returns the directory path for the hero.
    """
    for hero in HERO_MAP:
        names = [hero['name'], *hero['old_names']]
        names = list(map(str.lower, names))

        if hero_name in names:
            return HEROES_DIR / hero['dir']
    else:
        raise ValueError(f"Hero {hero_name} not found in HERO_MAP")