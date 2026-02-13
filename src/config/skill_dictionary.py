import json
import os

# Load skill dictionary from JSON
config_path = os.path.join(os.path.dirname(__file__), "skill_dictionary.json")
with open(config_path, "r") as f:
    SKILL_DICT = json.load(f)
