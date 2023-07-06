from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TokenModel(BaseModel):
    token: str

@router.post("/set-token")
async def set_token(token: TokenModel):
    with open('token.txt', 'wb') as file:
        file.write(bytes(token.token, 'utf-8'))

    return {"message": "Token received"}
