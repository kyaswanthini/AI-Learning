from google import genai

client = genai.Client(api_key="AIzaSyD09GaJTholBj2qjAmWcWRhhng80xez4Kw")

with open("resume.txt", "r") as f:
    resume = f.read()

with open("job.txt", "r") as f:
    job = f.read()

prompt = f"""
You are an expert HR AI assistant.

Analyze this resume against the job description.

Resume:
{resume}

Job Description:
{job}

Return:
1. Match score (0-100)
2. Matched skills
3. Missing skills
4. Suggestions
5. Hiring recommendation
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n===== AI RESUME ANALYZER =====\n")
print(response.text)