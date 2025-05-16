from sqlalchemy.orm import Session
from app.models.store import Store  # предполагается, что у тебя есть модель Store
from app.schemas.store import StoreCreate

class CRUDStore:
    def create(self, db: Session, store_create: StoreCreate, owner_id: int):
        db_store = Store(
            name=store_create.name,
            description=store_create.description,
            owner_id=owner_id,
        )
        db.add(db_store)
        db.commit()
        db.refresh(db_store)
        return db_store

crud_store = CRUDStore()
