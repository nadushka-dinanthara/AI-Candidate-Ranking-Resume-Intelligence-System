def explain_ranking(candidate, jd_text):
    """
    Provide a simple explanation of why a candidate was ranked.
    Example output:
    - Matching skills
    - Years of experience
    - Education level
    """
    explanation = []

    # Skills
    skills = candidate.get("skills", [])
    if skills:
        explanation.append(f"Matched skills: {', '.join(skills)}")

    # Experience
    exp = candidate.get("experience", 0)
    explanation.append(f"Years of experience: {exp}")

    # Education
    edu = candidate.get("education", [])
    if edu:
        explanation.append(f"Education: {', '.join(edu)}")

    # Score
    score = candidate.get("score", 0)
    explanation.append(f"Final Score: {score:.2f}")

    return "\n".join(explanation)
