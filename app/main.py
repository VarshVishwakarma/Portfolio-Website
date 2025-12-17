import os
import time
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from groq import Groq

app = FastAPI()

# 1. Mount Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 2. Setup Templates
templates = Jinja2Templates(directory="app/templates")

# 3. Setup Groq API (Ensure you set your Key!)
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY") or "gsk_YOUR_ACTUAL_API_KEY_HERE"
)

class ChatRequest(BaseModel):
    message: str

# --- ROUTES ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/playground", response_class=HTMLResponse)
async def playground(request: Request):
    return templates.TemplateResponse("playground.html", {"request": request})

# ✅ THIS WAS MISSING -> The Architecture Route
@app.get("/architecture", response_class=HTMLResponse)
async def architecture(request: Request):
    return templates.TemplateResponse("architecture.html", {"request": request})

# --- API ROUTES ---

@app.post("/api/chat")
async def chat_endpoint(chat_request: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are Varsh.AI. Concise, technical, futuristic."},
                {"role": "user", "content": chat_request.message}
            ],
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}