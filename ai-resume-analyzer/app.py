# app.py

from utils import load_text, extract_skills, match_skills

# Load files
resume_text = load_text("resume.txt")
job_text = load_text("job.txt")

# Extract skills
resume_skills = extract_skills(resume_text)

# Match
matched, missing, score = match_skills(resume_skills, job_text)

# Output
print("\n===== AI RESUME ANALYZER =====\n")

print("Matched Skills:")
for skill in matched:
    print(f"✔ {skill}")

print("\nMissing Skills:")
for skill in missing:
    print(f"❌ {skill}")

print(f"\nResume Match Score: {score}%")

# Suggestions
print("\nSuggestions:")
if score < 50:
    print("⚠️ Improve your skills for this job")
elif score < 80:
    print("👍 Good match, but some improvements needed")
else:
    print("🔥 Excellent match! You are a strong candidate")