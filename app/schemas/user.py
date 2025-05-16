from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    phone: str
    email: EmailStr  # Добавляем поле email с проверкой формата

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True
