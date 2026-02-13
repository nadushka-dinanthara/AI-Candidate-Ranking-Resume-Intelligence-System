import streamlit as st
import matplotlib.pyplot as plt

def skill_distribution_chart(candidates):
    """
    Display a bar chart of top skills among candidates.
    """
    skill_counts = {}
    for c in candidates:
        for skill in c.get("skills", []):
            skill_counts[skill] = skill_counts.get(skill, 0) + 1

    if skill_counts:
        skills = list(skill_counts.keys())
        counts = list(skill_counts.values())
        plt.figure(figsize=(10,5))
        plt.bar(skills, counts, color='skyblue')
        plt.xticks(rotation=45)
        plt.title("Skill Distribution Among Candidates")
        st.pyplot(plt)
