from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})

@router.get("/projects")
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request, "title": "Projects"})

# --- NEW ROUTES ---
@router.get("/playground")
async def playground(request: Request):
    return templates.TemplateResponse("playground.html", {"request": request, "title": "AI Terminal"})

@router.get("/docs-site")
async def docs(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request, "title": "Documentation"})