def extract_education(text):
    """
    Extract education keywords from text.
    Simple keyword-based extraction: bachelor, master, phd, diploma
    """
    edu_keywords = ["bachelor", "master", "phd", "diploma", "associate"]
    found_edu = [word for word in edu_keywords if word in text.lower()]
    return found_edu
