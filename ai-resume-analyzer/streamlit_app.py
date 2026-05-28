import streamlit as st
from google import genai

client = genai.Client(api_key="YOUR_API_KEY_HERE")

st.title("🤖 AI Resume Analyzer")

resume_file = st.file_uploader("Upload Resume", type=["txt"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if resume_file and job_desc:

        resume = resume_file.read().decode("utf-8")

        prompt = f"""
        You are an expert HR AI assistant.

        Resume:
        {resume}

        Job Description:
        {job_desc}

        Give:
        1. Match score
        2. Matched skills
        3. Missing skills
        4. Suggestions
        5. Recommendation
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.subheader("AI Analysis")
        st.write(response.text)

    else:
        st.warning("Please upload resume and job description")