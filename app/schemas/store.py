from pydantic import BaseModel
from typing import Optional

class StoreBase(BaseModel):
    name: str
    description: Optional[str] = None

class StoreCreate(StoreBase):
    pass

class StoreRead(StoreBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
