from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.store import StoreCreate, StoreRead
from app.crud.crud_store import crud_store
from auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/stores/", response_model=StoreRead)
def create_store(store_create: StoreCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_store.create(db, store_create, owner_id=current_user.id)
