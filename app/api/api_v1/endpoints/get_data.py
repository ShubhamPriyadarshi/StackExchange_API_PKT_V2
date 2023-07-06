import httpx
from fastapi import APIRouter

router = APIRouter()

@router.get("/data")
async def get_data():
    # Read the encrypted access token from the file
    with open('token.txt','r', encoding='utf-8') as file:
        access_token = file.read()

    if not access_token:
        return {"message": "Access token not available. Please authenticate first."}

    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.stackexchange.com/2.3/tags?order=desc&sort=popular&site=stackoverflow", headers=headers)
        data = response.json()

        return data
