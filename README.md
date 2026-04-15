# MediMind AI (Groq Version)

MediMind AI is a lightweight healthcare assistant API that analyzes user symptoms and provides general health insights using a large language model. It is designed for learning, experimentation, and demonstration purposes.

## Features

* Symptom analysis using LLM
* Basic triage (Low / Medium / Emergency)
* Emergency keyword detection
* REST API built with FastAPI
* Simple and modular project structure

## Tech Stack

* Python
* FastAPI
* Groq API (LLaMA 3 model)
* Uvicorn
* python-dotenv

## Project Structure

medimind-ai-groq/
│── main.py          # FastAPI entry point
│── agent.py         # AI interaction logic
│── triage.py        # Emergency detection logic
│── requirements.txt # Dependencies
│── .env             # API key (not committed)
│── README.md

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/medimind-ai-groq.git

2. Navigate to the project folder:
   cd medimind-ai-groq

3. Create a virtual environment (optional but recommended):
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

## Environment Variables

Create a `.env` file in the root directory and add:

GROQ_API_KEY=your_api_key_here

Do not commit this file to version control.

## Running the Application

Start the FastAPI server using:

uvicorn main:app --reload

The API will be available at:
http://127.0.0.1:8000

Interactive API docs:
http://127.0.0.1:8000/docs

## API Endpoints

GET /

* Returns a simple status message

POST /analyze

* Analyzes user symptoms

Request body:
{
"symptoms": "fever, headache, cough"
}

Response:
{
"triage": "No immediate emergency detected.",
"analysis": "Possible conditions include..."
}

## How It Works

1. User sends symptoms via API
2. Triage module checks for emergency keywords
3. AI agent sends prompt to Groq LLM
4. Model generates possible conditions and advice
5. API returns combined response

## Disclaimer

This project does not provide medical diagnosis.
It is intended for educational purposes only.
Always consult a qualified healthcare professional for medical advice.

## Future Improvements

* User health history tracking
* Authentication system
* Frontend dashboard (React)
* File upload for medical reports
* Multi-agent system (doctor, nutrition, fitness)

## License

This project is open-source and available under the MIT License.

## Author

Jai Pratap Singh
