import streamlit as st

def show_candidate_details(candidate):
    """
    Display detailed info about a single candidate.
    """
    st.subheader(candidate["filename"])
    st.write("**Skills:**", ", ".join(candidate.get("skills", [])))
    st.write("**Experience:**", candidate.get("experience", "N/A"))
    st.write("**Education:**", candidate.get("education", "N/A"))
    st.write("**Raw Text Preview:**")
    st.text(candidate.get("text", "")[:500] + "...")
