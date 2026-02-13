import streamlit as st
from components.ranking_table import display_rankings
from utils.ui_helpers import format_score
from src.parsing.resume_parser import parse_resume
from src.parsing.jd_parser import parse_jd
from src.features.skill_extractor import extract_skills
from src.features.experience_extractor import extract_experience
from src.features.education_extractor import extract_education
from src.scoring.scoring_engine import rank_candidates

def main():
    st.title("AI Candidate Ranking & Resume Intelligence System")

    # Upload Job Description
    uploaded_jd = st.file_uploader("Upload Job Description", type=["pdf","docx","txt"])

    # Upload Candidate Resumes
    uploaded_cvs = st.file_uploader(
        "Upload Candidate Resumes", accept_multiple_files=True, type=["pdf","docx","txt"]
    )

    if uploaded_jd and uploaded_cvs:
        # Parse JD
        jd_text = parse_jd(uploaded_jd)

        # Parse CVs and extract features
        candidates = []
        for cv_file in uploaded_cvs:
            text = parse_resume(cv_file)
            skills = extract_skills(text)
            experience = extract_experience(text)
            education = extract_education(text)
            candidates.append({
                "filename": cv_file.name,
                "text": text,
                "skills": skills,
                "experience": experience,
                "education": education
            })

        # Rank candidates
        ranked_candidates = rank_candidates(candidates, jd_text)

        # Display rankings
        display_rankings(ranked_candidates)

if __name__ == "__main__":
    main()
