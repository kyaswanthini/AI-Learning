import os
from google import genai

# Create Gemini client using environment variable
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Read files
with open("resume.txt", "r") as f:
    resume = f.read()

with open("job.txt", "r") as f:
    job = f.read()

# Prompt for AI
prompt = f"""
You are an expert HR AI assistant.

Compare the resume with the job description and return:

1. Match score (0-100)
2. Matched skills
3. Missing skills
4. Suggestions
5. Hiring recommendation

---

Resume:
{resume}

---

Job Description:
{job}
"""

# Call Gemini model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# Output result
print("\n===== AI RESUME ANALYZER =====\n")
print(response.text)