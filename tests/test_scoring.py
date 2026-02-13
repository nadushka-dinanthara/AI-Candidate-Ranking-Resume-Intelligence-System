from src.scoring.scoring_engine import rank_candidates

def test_rank_candidates():
    candidates = [
        {"filename": "a.txt", "text": "Python developer", "skills": ["Python"], "experience": 3, "education": ["bachelor"]},
        {"filename": "b.txt", "text": "Java developer", "skills": ["Java"], "experience": 5, "education": ["master"]}
    ]
    jd_text = "Looking for a Python developer"
    
    ranked = rank_candidates(candidates, jd_text)
    
    # The first candidate should be ranked higher
    assert ranked[0]["filename"] == "a.txt"
