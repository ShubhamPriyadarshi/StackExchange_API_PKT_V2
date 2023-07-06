from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/display-token")
async def display_token(request: Request, token: str):
    return templates.TemplateResponse("display_token.html", {"request": request, "token": token})
