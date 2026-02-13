# app/app.py
import streamlit as st
from components.ranking_table import display_rankings
from src.parsing.resume_parser import parse_resume
from src.parsing.jd_parser import parse_jd
from src.features.experience_extractor import extract_experience
from src.features.education_extractor import extract_education
from src.scoring.scoring_engine import rank_candidates

st.set_page_config(page_title="AI Candidate Ranking", layout="wide")
st.title("🤖 AI Candidate Ranking & Resume Intelligence System")
st.markdown("---")

# Sidebar: Job Description upload
uploaded_jd = st.sidebar.file_uploader("Upload Job Description (PDF/TXT/DOCX)", type=["pdf","txt","docx"])

# Main: Candidate Resumes upload
uploaded_cvs = st.file_uploader("Upload Candidate Resumes", accept_multiple_files=True)

if uploaded_jd and uploaded_cvs:
    # Parse JD
    jd_text = parse_jd(uploaded_jd)

    # Parse CVs
    candidates = []
    for cv_file in uploaded_cvs:
        cv_text = parse_resume(cv_file)
        candidates.append({
            "filename": cv_file.name,
            "text": cv_text,
            "experience": extract_experience(cv_text),
            "education": extract_education(cv_text)
        })

    # Rank candidates
    ranked_candidates = rank_candidates(candidates, jd_text)

    # Display Rankings
    st.subheader("Candidate Rankings")
    display_rankings(ranked_candidates)

    # Candidate Details
    st.subheader("Candidate Details")
    candidate_names = [c["filename"] for c in ranked_candidates]
    selected = st.selectbox("Select a candidate to view details", candidate_names)
    candidate = next(c for c in ranked_candidates if c["filename"] == selected)
    
    st.markdown(f"**Experience:** {candidate['experience']} years")
    st.markdown(f"**Education:** {', '.join(candidate['education'])}")
