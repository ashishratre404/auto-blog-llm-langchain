# BlogPilot API

This is the backend service for BlogPilot, an AI-powered blog generator built with FastAPI and LangChain.

## 🚀 Setup Instructions

1. Clone (If not already)
```bash
git clone https://github.com/your-username/auto-blog-agent.git
cd auto-blog-agent
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Add your OpenAI API key in ```bash .env```:
```bash
OPENAI_API_KEY=your-api-key-here
```

🏃 Start the Server
```bash 
uvicorn main:app --reload
```

API will be available at:
http://localhost:8000/generate-blog


## 📦 Endpoint
POST /generate-blog

Request Body:
```bash
{
  "topic": "ai in healthcare"
}
```
Response:
```bash
{
  "title": "...",
  "intro": "...",
  "mainContent": "...",
  "summary": "..."
}
```
