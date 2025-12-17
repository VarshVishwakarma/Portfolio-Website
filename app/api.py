from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import views, api

# This is the 'app' variable Uvicorn is looking for
app = FastAPI()

# Connects the CSS/JS folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Connects the web pages (views) and the logic (api)
app.include_router(views.router)
app.include_router(api.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)