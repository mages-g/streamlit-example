import streamlit as st
import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import matplotlib.pyplot as plt

# Download NLTK resources if not downloaded already
nltk.download('punkt')
nltk.download('stopwords')

# Sample DataFrame (Replace this with your actual DataFrame)
file_path = 'C:\\Users\\govin\\OneDrive\\Desktop\\Python\\Linkedin_job_postings\\data.csv'
df = pd.read_csv(file_path)
common_words = ['data', 'experience', 'business', 'work', 'skills', 'including', 'ability', 'new',
    'years', 'job', 'information', 'time', 'status', 'using', 'across', 'us', 'based',
    'may', 'well', 'please', 'multiple', 'also', 'best', 'day', 'take', 'action', 'without',
    'following', 'use', 'learn', 'problems', 'etc', 'primary', 'activities', 'specific',
    'etc', 'etcetera', 'including', 'various', 'such', 'able', 'within', 'without', 'days',
    'following', 'based', 'clients', 'requirements', 'provide', 'systems', 'services', 'needs',
    'individual', 'related', 'using', 'related', 'various', 'multiple', 'related', 'skills',
    'us', 'must', 'may', 'etc', 'including', 'etcetera', 'based', 'role', 'etcetera',
    "including", "us", "candidates", "tools", "support", "key", "development", "products", "environment",
    "systems", "marketing", "information", "time", "customer", "financial", "employer", "communication",
    "knowledge", "office", "requirements", "services", "healthcare", "education", "strategy", "salary", "employee",
    "equal", "opportunities", "process", "projects", "science", "tableau", "industry",
    "insurance", "microsoft", "compensation", "quality", "field", "race", "orientation", "health", "vulnerability",
    "risk", "technology", "research", "computer", "national", "sexual", "veteran", "design", "change", "leadership",
    "sets", "translate", "join", "external", "manage", "written", "religion", "platforms", "legal", "background",
    "successful", "department", "minimum", "user", "hours", "leave", "law", "apply", "qualified", "compliance",
    "visualization", "competitive", "dashboards", "actionable", "career", "global", "diversity", "value", "innovative",
    "existing", "workforce", "mission", "operational", "finance", "description", "advanced", "functions", "meet",
    "responsible", "passionate", "decisions", "goals", "market", "success", "local", "governance", "contract",
    "remote", "building", "identity", "directly", "areas", "plus", "culture", "detail", "current", "excellent",
    "policy", "flexible", "digital", "factors", "anime", "grail", "enterprise", "findings", "level", "problem",
    "expected", "overall", "modeling", "results", "analyzing", "technologies", "monthly", "duties",
    "discriminate", "age", "sales", "analyses", "appropriate", "models", "ad", "includes", "statistics", "google",
    "least", "ally", "credit", "hiring", "community", "datasets", "assistance", "applicable", "transportation",
    "planning", "note", "source", "maintain", "interact", "hybrid", "training", "strategies", "departments",
    "focus", "organizational", "additional", "available", "initiatives", "order", "mathematics", "similar", "sas",
    "application", "programming", "curiosity", "consulting", "energy", "questions", "dynamic", "enhance", "potential",
    "expertise", "attention", "posted", "way", "better", "efficiency", "serve", "focused", "offers", "fans",
    "great", "maintains", "government", "sdot", "inclusion", "quantitative", "interpret",
    "equivalent", "levels", "experiences", "prior", "plans", "detailed", "direct", "essential", "contribute",
    "collaborate", "considered", "week", "big", "visit", "groups", "build", "control", "expert",
    "comfortable", "languages", "comprehensive", "sex", "high", "effectiveness", "etl", "real", "package", "leading",
    "patterns", "hoc", "applying", "variety", "rewards", "via", "values", "vaccination", "vendors", "implement",
    "center", "revenue", "personal", "content", "monitor", "marital", "different", "commitment", "receive",
    "regular", "sony", "total", "marketplace", "bonus", "frontdoor", "equipmentshare", "achieving", "rcm", "claim",
    "duration", "modelling", "executive", "combination", "term", "warehouse", "ls", "growing", "provides", "relationships",
    "visualizations", "documentation", "optimize", "mindset", "continuous", "consider", "https", "managers", "collection",
    "engineering", "objectives", "priorities", "area", "positions", "environments", "consistent", "methods", "tasks",
    "suite", "legally", "ask", "behavior", "indicators", "important", "units", "execute", "communities", "check",
    "improvements", "asset", "maintenance", "experienced", "conduct", "partner", "future", "pto", "savings", "retirement",
    "consumer", "programs", "entire", "applications", "develops", "dependent", "end", "seattle", "designed", "francisco",
    "extract", "email", "app", "supply", "earnings", "participate", "automated", "family", "certification", "annual",
    "companies", "dish", "coordination", "requirement", "transform", "completed", "pittsburgh", "federal", "privacy",
    "statement", "protection", "policies", "regulated", "proficiency", "combine", "continuously", "orally", "legislation",
    "skills", "passion", "use", "leads", "plus", "competitive", "compensation", "offers", "employment", "data", "time",
    "opportunity", "team", "business", "company", "years", "management", "information", "skills", "ability", "job",
    "position", "status", "development", "candidate", "degree", "teams", "responsibilities", "product", "processes",
    "employer", "people", "communication", "insights", "project", "role", "location", "pay", "knowledge", "system",
    "office", "needs", "qualifications"
]

def get_skills(job_descriptions, num_skills):
    all_skills = []
    stop_words = set(stopwords.words('english'))
    stop_words.update(common_words)
    
    for job_desc in job_descriptions:
        tokens = word_tokenize(job_desc.lower())
        tokens = [token for token in tokens if token not in stop_words and token.isalpha()]
        all_skills.extend(tokens)
    
    skill_counts = Counter(all_skills)
    most_common_skills = skill_counts.most_common(num_skills)
    
    # Sort skills by occurrence count
    most_common_skills = sorted(most_common_skills, key=lambda x: x[1], reverse=True)
    
    return most_common_skills

def get_companies_for_job_title(job_title, num_companies):
    related_companies = df[df['job_title'].str.contains(job_title, case=False)]['company_name'].tolist()
    return related_companies[:num_companies]

def main():
    st.title('Resume Terms Deriver 2 (RTD2)')

    user_input = st.text_input("Enter a job designation:")

    num_options = [10, 30, 50, 100]
    num_display = st.selectbox("Select number of items to display:", num_options)

    if st.button('Find Skills'):
        filtered_df = df[df['job_title'].str.contains(user_input, case=False)]
        job_descriptions = filtered_df['job_description'].tolist()

        if job_descriptions:
            most_common_skills = get_skills(job_descriptions, num_display)
            skills_string = ", ".join([skill[0] for skill in most_common_skills])
            st.write(f"Include these skills to your resume for max relevance: {skills_string}")

            # Plot top 30 skills sorted by occurrence count
            top_skills = dict(sorted(dict(most_common_skills[:30]).items(), key=lambda item: item[1], reverse=True))
            plt.figure(figsize=(10, 8))
            plt.barh(list(top_skills.keys()), list(top_skills.values()))
            plt.xlabel('Frequency')
            plt.title('Top 30 Common Skills (Sorted)')
            st.pyplot(plt)

        else:
            st.write("No job descriptions found for the given job title.")

    if st.button('Find Companies'):
        num_companies = num_display  # Adjust this if needed
        related_companies = get_companies_for_job_title(user_input, num_companies)
        
        if related_companies:
            companies_string = ", ".join(related_companies)
            st.write(f"Companies related to the input job title: {companies_string}")
        else:
            st.write("No companies found for the given job title.")

if __name__ == "__main__":
    main()