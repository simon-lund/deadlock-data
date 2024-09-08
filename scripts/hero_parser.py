import json

from config import RAW_DATA_DIR, HERO_MAP
from utils import download, get_hero_dir

# Download heroes.vdata.json file
raw_heroes_file_url = "https://raw.githubusercontent.com/ouwou/deadlock-data-tracking/master/data/heroes.vdata.json"
raw_heroes_file = RAW_DATA_DIR / "heroes.vdata.json"
download(raw_heroes_file_url, raw_heroes_file)

# Download abilities.vdata.json file
raw_ability_file_url = "https://raw.githubusercontent.com/ouwou/deadlock-data-tracking/master/data/abilities.vdata.json"
raw_ability_file = RAW_DATA_DIR / "abilities.vdata.json"
download(raw_ability_file_url, raw_ability_file)

# Download citadel_heroes_english.txt file (Translations)
raw_translations_file_url = "https://raw.githubusercontent.com/SteamDatabase/GameTracking-Deadlock/master/game/citadel/resource/localization/citadel_heroes/citadel_heroes_english.txt"
raw_translations_file = RAW_DATA_DIR / "citadel_heroes_english.txt"
download(raw_translations_file_url, raw_translations_file)

# Select current heroes
raw_heroes_data = json.loads(raw_heroes_file.read_text())['Root']
heroes = {}
hero_dirs = {}
for hero_name, hero_data in raw_heroes_data.items():
    if not hero_name.startswith("hero_"):
        continue

    hero_name = hero_name.replace("hero_", "")
    try:
        hero_dir = get_hero_dir(hero_name)
    except KeyError:
        continue

    if hero_dir.exists():
        heroes[hero_dir.name] = hero_data
        hero_dirs[hero_dir.name] = hero_dir

# Expect len(HERO_MAP) == len(heroes)
assert len(HERO_MAP) == len(heroes), f"Expected {len(HERO_MAP)} heroes, got {len(heroes)}"

# Keys for standard level upgrades
# (not all heroes have all of these keys, but this is the full list, so we can have 'null' values for missing keys)
standard_level_upgrades_keys = list(set(
    key
    for hero in heroes
    for key in heroes[hero]["m_mapStandardLevelUpUpgrades"].keys()
))

# Extract hero data from heroes.vdata.json
for hero in heroes:
    hero_dir = hero_dirs[hero]
    hero_file = hero_dir / "data.json"
    hero_data = heroes[hero]

    hero_json = json.loads(hero_file.read_text())

    hero_json["id"] = hero_data["m_HeroID"]
    hero_json["new_player_friendly"] = hero_data.get("m_bNewPlayerFriendly", False)

    # Starting stats
    starting_stats = hero_data["m_mapStartingStats"]
    hero_json["starting_stats"] = {
        "max_move_speed": starting_stats["EMaxMoveSpeed"],
        "sprint_speed": starting_stats["ESprintSpeed"],
        "crouch_speed": starting_stats["ECrouchSpeed"],
        "move_acceleration": starting_stats["EMoveAcceleration"],
        "light_melee_damage": starting_stats["ELightMeleeDamage"],
        "heavy_melee_damage": starting_stats["EHeavyMeleeDamage"],
        "max_health": starting_stats["EMaxHealth"],
        "weapon_power": starting_stats["EWeaponPower"],
        "reload_speed": starting_stats["EReloadSpeed"],
        "weapon_power_scale": starting_stats["EWeaponPowerScale"],
        "stamina": starting_stats["EStamina"],
        "base_health_regen": starting_stats["EBaseHealthRegen"],
        "stamina_regen_per_second": starting_stats["EStaminaRegenPerSecond"],
    }

    # Ability names
    abilities = hero_data["m_mapBoundAbilities"]
    hero_json["abilities"] = [abilities[f"ESlot_Signature_{i}"] for i in range(1, 5)]

    # Standard level upgrades
    standard_level_upgrades = hero_data["m_mapStandardLevelUpUpgrades"]
    hero_json["level_upgrades"] = {key.lower(): standard_level_upgrades.get(key, None) for key in standard_level_upgrades_keys}

    # Save hero data
    hero_file.write_text(json.dumps(hero_json, indent=4))