import re
import string

def clean_text(text):
    """
    Basic text cleaning:
    - Lowercase
    - Remove extra spaces, newlines, tabs
    - Remove punctuation
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)         # Replace multiple spaces/newlines with single space
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()
