from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_products():
    return {"message": "Products route is working"}
