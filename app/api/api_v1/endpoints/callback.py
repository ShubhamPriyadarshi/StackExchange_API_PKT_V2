from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/auth-callback")
async def auth_callback(request: Request):
    return templates.TemplateResponse("callback.html", {"request": request})
