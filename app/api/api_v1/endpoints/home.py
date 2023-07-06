from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.core.auth import authenticate

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def home(request: Request):
    auth_url = await authenticate()
    return templates.TemplateResponse("index.html", {"request": request, "auth_url": auth_url})
