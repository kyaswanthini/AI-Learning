import os
import streamlit as st
from google import genai

# Page settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="centered"
)

# Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Title
st.title("🤖 AI Resume Analyzer")
st.markdown("Analyze resumes against job descriptions using Gemini AI")

# Resume upload
resume_file = st.file_uploader(
    "📄 Upload Resume (.txt)",
    type=["txt"]
)

# Job description
job_desc = st.text_area(
    "💼 Paste Job Description",
    height=200
)

# Analyze button
if st.button("🚀 Analyze Resume"):

    if resume_file and job_desc:

        with st.spinner("Analyzing resume..."):

            resume = resume_file.read().decode("utf-8")

            prompt = f"""
            You are an expert HR AI assistant.

            Compare the resume with the job description.

            Return:
            1. Match score
            2. Matched skills
            3. Missing skills
            4. Suggestions
            5. Hiring recommendation

            Resume:
            {resume}

            Job Description:
            {job_desc}
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.success("Analysis Complete ✅")

            st.subheader("📊 AI Analysis Result")
            st.write(response.text)

    else:
        st.warning("Please upload resume and enter job description.")