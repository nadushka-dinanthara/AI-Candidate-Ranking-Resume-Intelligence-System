def weighted_score(skill_score, experience_score, education_score, weights=None):
    """
    Combine different factors into a final score.
    weights: dict with keys 'skills', 'experience', 'education'
    """
    if weights is None:
        weights = {"skills": 0.5, "experience": 0.3, "education": 0.2}

    final_score = (
        skill_score * weights["skills"] +
        experience_score * weights["experience"] +
        education_score * weights["education"]
    )
    return final_score
