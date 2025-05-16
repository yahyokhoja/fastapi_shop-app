from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_shops():
    return {"message": "Shops route is working"}
