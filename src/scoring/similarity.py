from src.features.embeddings import get_embedding, cosine_sim

def compute_similarity(candidate_text, jd_text):
    """
    Compute similarity score between candidate resume and JD.
    Returns a float score between 0 and 1.
    """
    candidate_vec = get_embedding(candidate_text)
    jd_vec = get_embedding(jd_text)
    score = cosine_sim(candidate_vec, jd_vec)
    return score
