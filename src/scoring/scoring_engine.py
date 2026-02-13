# src/scoring/scoring_engine.py
from src.features.embeddings import get_embedding
from sklearn.metrics.pairwise import cosine_similarity

def rank_candidates(candidates, jd_text):
    """
    Rank candidates based on similarity to the job description.
    candidates: list of dicts with keys: filename, text, experience, education
    jd_text: string
    Returns: list of dicts with filename, score, experience, education
    """
    jd_emb = get_embedding(jd_text)
    ranked = []

    for c in candidates:
        cv_emb = get_embedding(c["text"])
        score = float(cosine_similarity([jd_emb], [cv_emb])[0][0])
        ranked.append({
            "filename": c["filename"],
            "score": score,
            "experience": c.get("experience", 0),
            "education": c.get("education", [])
        })

    # Sort descending by score
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked
