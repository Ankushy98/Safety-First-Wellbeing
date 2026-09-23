from fastapi import FastAPI

from .database.database import Base, engine
from .database import models
from .routes.journal import router as journal_router
from .routes.referral import router as referral_router
from .routes.admin import router as admin_router
from .routes.privacy import router as privacy_router
from fastapi.templating import Jinja2Templates
from fastapi import Request

Base.metadata.create_all(bind=engine)


app = FastAPI(
    templates = Jinja2Templates(directory="app/templates"),
    title="Safety-First Wellbeing Agent",
    description="Safety-first wellbeing conversational system",
    version="1.0.0"
)
templates = Jinja2Templates(directory="app/templates")

app.include_router(journal_router)
app.include_router(referral_router)
app.include_router(admin_router)
app.include_router(privacy_router)


@app.get("/")
def home():
    return {
        "message": "Safety-First Wellbeing Agent is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={}
    )

@app.get("/admin-dashboard")
def admin_dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={}
    )

@app.get("/audit-dashboard")
def audit_dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="audit.html",
        context={}
    )