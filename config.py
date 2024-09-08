import json
from pathlib import Path

ROOT_DIR = Path(__file__).parent

RAW_DATA_DIR = ROOT_DIR / "raw"
RAW_DATA_DIR.mkdir(exist_ok=True)

DATA_DIR = ROOT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

HEROES_DIR = DATA_DIR / "heroes"
HEROES_DIR.mkdir(exist_ok=True)

WIKI_BASE_URL = 'https://deadlocked.wiki'

with open(HEROES_DIR / "hero_map.json") as f:
    HERO_MAP = json.load(f)
