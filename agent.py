import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_symptoms(symptoms):
    prompt = f"""
    You are a healthcare AI assistant.

    Analyze the symptoms: {symptoms}

    Provide:
    1. Possible conditions (not a diagnosis)
    2. Severity level (Low / Medium / Emergency)
    3. Basic advice
    Keep it simple and clear.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content