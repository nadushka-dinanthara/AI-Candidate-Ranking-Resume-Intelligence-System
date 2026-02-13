import re

def extract_experience(text):
    """
    Extract years of experience from text.
    Simple regex to find patterns like '3 years', '5+ yrs', etc.
    """
    matches = re.findall(r'(\d+)\s*(\+?\s*years|yrs|year|yr)', text, flags=re.IGNORECASE)
    total_exp = 0
    for match in matches:
        total_exp += int(match[0])
    return total_exp
