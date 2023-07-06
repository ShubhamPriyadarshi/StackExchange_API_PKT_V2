from fastapi import APIRouter
from app.tasks.load_data_task import DataLoader
router = APIRouter()

# @router.get("/load-data")
# async def load_data():
#     await main()
#     return {"message": "Data loading In Progress"}
@router.get("/load-data")
async def load_data():
    await DataLoader.load_data()
    return {"message": "Data loading in progress"}
