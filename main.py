from fastapi import FastAPI
from agent import analyze_symptoms
from triage import check_emergency

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MediMind AI (Groq) is running"}

@app.post("/analyze")
def analyze(data: dict):
    symptoms = data.get("symptoms")

    triage = check_emergency(symptoms)
    ai_response = analyze_symptoms(symptoms)

    return {
        "triage": triage,
        "analysis": ai_response
    }