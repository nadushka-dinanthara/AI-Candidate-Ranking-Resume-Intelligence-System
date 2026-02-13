import json
from src.config.skill_dictionary import SKILL_DICT

def extract_skills(text):
    """
    Extract skills from text based on a predefined skill dictionary.
    Returns a list of skills found in the candidate text.
    """
    found_skills = []
    for category, skills in SKILL_DICT.items():
        for skill in skills:
            if skill.lower() in text:
                found_skills.append(skill)
    return list(set(found_skills))
