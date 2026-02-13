import streamlit as st

def display_rankings(ranked_candidates):
    """
    Display ranked candidates in a table.
    """
    table_data = []
    for i, c in enumerate(ranked_candidates, 1):
        table_data.append({
            "Rank": i,
            "Candidate": c["filename"],
            "Score": round(c.get("score", 0), 2),
            "Top Skills": ", ".join(c.get("skills", []))
        })
    st.table(table_data)
