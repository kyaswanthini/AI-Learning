# utils.py

def load_text(file_path):
    with open(file_path, "r") as file:
        return file.read().lower()

def extract_skills(text):
    return set([skill.strip() for skill in text.split(",")])

def match_skills(resume_skills, job_text):
    matched = []
    missing = []

    for skill in resume_skills:
        if skill.lower() in job_text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = len(matched) / len(resume_skills) * 100

    return matched, missing, round(score, 2)