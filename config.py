from pathlib import Path

import json


ROOT_DIR = Path(__file__).parent

DATA_DIR = ROOT_DIR / "data"

HEROES_DIR = DATA_DIR / "heroes"

WIKI_BASE_URL = 'https://deadlocked.wiki'

with open(HEROES_DIR / "hero_map.json") as f:
    HERO_MAP = json.load(f)