from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_orders():
    return {"message": "Orders route is working"}
