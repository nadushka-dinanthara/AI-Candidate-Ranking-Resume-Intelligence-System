# app/components/ranking_table.py
import streamlit as st

def display_rankings(ranked_candidates):
    """
    Display ranked candidates in a table.
    Expects a list of dictionaries with keys: filename, score, experience, education
    """
    table_data = []

    for i, c in enumerate(ranked_candidates, 1):
        filename = c.get("filename", "N/A")
        score = round(c.get("score", 0), 2)
        experience = c.get("experience", "N/A")
        education = ", ".join(c.get("education", []))

        table_data.append({
            "Rank": i,
            "Candidate": filename,
            "Score": score,
            "Experience": experience,
            "Education": education
        })

    st.table(table_data)
