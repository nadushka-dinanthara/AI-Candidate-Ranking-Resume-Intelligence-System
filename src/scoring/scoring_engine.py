from src.scoring.similarity import compute_similarity
from src.scoring.weighting import weighted_score

def rank_candidates(candidates, jd_text):
    """
    Rank candidates based on similarity to JD and other factors.
    Returns a list of candidates sorted by score.
    """
    for c in candidates:
        # Compute similarity score
        sim_score = compute_similarity(c["text"], jd_text)

        # Compute simple feature-based scores
        skill_score = len(c.get("skills", [])) / 10  # normalize to ~0-1
        exp_score = min(c.get("experience", 0)/10, 1) # cap at 1
        edu_score = min(len(c.get("education", []))/3, 1)

        # Weighted final score
        c["score"] = weighted_score(skill_score, exp_score, edu_score)
        # Optional: combine with similarity
        c["score"] = 0.7 * c["score"] + 0.3 * sim_score

    # Sort descending by score
    ranked = sorted(candidates, key=lambda x: x["score"], reverse=True)
    return ranked
