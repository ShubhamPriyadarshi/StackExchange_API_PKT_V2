from fastapi import APIRouter
from app.api.api_v1.endpoints import home, callback, set_token, display_token, load_data, get_data

api_router = APIRouter()
api_router.include_router(home.router, tags=["home"])
api_router.include_router(callback.router, tags=["callback"])
api_router.include_router(set_token.router, tags=["set_token"])
api_router.include_router(display_token.router, tags=["display_token"])
api_router.include_router(load_data.router, tags=["load_data"])
api_router.include_router(get_data.router, tags=["get_data"])
