def check_emergency(symptoms):
    emergency_keywords = [
        "chest pain",
        "breathing difficulty",
        "unconscious",
        "severe bleeding",
        "stroke",
        "heart attack"
    ]

    for word in emergency_keywords:
        if word in symptoms.lower():
            return "🚨 EMERGENCY: Seek immediate medical help!"

    return "No immediate emergency detected."