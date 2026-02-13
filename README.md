# 🤖 AI Candidate Ranking & Resume Intelligence System

A **skill-free AI-powered candidate ranking system** that automatically evaluates and ranks candidates based on **job description similarity**.  
Designed for **Business Management, Marketing, HR, or any non-technical roles**, this system does not require a predefined skill list and works with any uploaded CVs.

---

## **Features**

- Upload a **Job Description (JD)** in PDF, TXT, or DOCX format.  
- Upload multiple **candidate CVs** at once.  
- Automatically **rank candidates** based on similarity to JD using embeddings.  
- Extract and display **experience** and **education** from CVs.  
- Clean **Streamlit UI** with ranking table and candidate details.  
- Fully **domain-independent**, no skill dictionary required.  

---

## **Project Structure**

candidate_ranking_system/
│
├── app/
│ ├── app.py # Streamlit app entry point
│ ├── components/
│ │ └── ranking_table.py # Display candidate rankings
│ └── utils/
│ └── ui_helpers.py # Optional UI formatting helpers
│
├── src/
│ ├── parsing/
│ │ ├── resume_parser.py # Parse PDF/TXT/DOCX CVs
│ │ └── jd_parser.py # Parse Job Description
│ │
│ ├── features/
│ │ ├── experience_extractor.py
│ │ └── education_extractor.py
│ │
│ ├── scoring/
│ │ └── scoring_engine.py # Rank candidates based on embeddings
│ │
│ └── config/ # Optional: config files (not needed for skill-free)
│
├── tests/ # Optional unit tests
├── requirements.txt
├── README.md
└── run.py # Optional entry point for Streamlit


---

## **Setup & Installation**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Candidate-Ranking-Resume-Intelligence-System.git
cd AI-Candidate-Ranking-Resume-Intelligence-System
Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Usage
Run the Streamlit app:

streamlit run app/app.py
Upload a Job Description (PDF/TXT/DOCX) in the sidebar.

Upload multiple CVs in the main area.

View ranked candidates in the table.

Select any candidate to see experience and education details.

How it Works
Each CV and the JD are converted into vector embeddings.

Cosine similarity is computed between each CV and the JD.

Candidates are ranked by similarity score.

Optional: Experience and Education are extracted for additional insights.