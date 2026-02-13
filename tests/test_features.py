from src.features.skill_extractor import extract_skills
from src.features.experience_extractor import extract_experience
from src.features.education_extractor import extract_education

def test_extract_skills():
    text = "I know Python, Java, and React"
    skills = extract_skills(text)
    assert "Python" in skills
    assert "Java" in skills

def test_extract_experience():
    text = "3 years in software development"
    exp = extract_experience(text)
    assert exp == 3

def test_extract_education():
    text = "I have a Bachelor in Computer Science"
    edu = extract_education(text)
    assert "bachelor" in edu
