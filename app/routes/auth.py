from fastapi import APIRouter, Depends, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.core.db import get_db
from app.schemas.user import UserCreate, UserRead
from app.crud.crud_user import crud_user
from auth import authenticate_user, create_access_token
from app.core.security import verify_password

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")  # укажи путь к шаблонам

# GET для страницы регистрации (отдаёт HTML форму)
@router.get("/register", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# POST для регистрации (создание пользователя)
@router.post("/register", response_model=UserRead)
def register(
    email: str = Form(...),
    phone: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Создаём объект UserCreate из формы
    user_create = UserCreate(email=email, phone=phone, password=password)

    # Проверяем, есть ли уже пользователь с таким email
    db_user = crud_user.get_by_email(db, email=user_create.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Создаём пользователя
    user = crud_user.create(db, user_create)
    return user

# GET для страницы логина (отдаёт HTML форму)
@router.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# POST для логина с формой
@router.post("/login")
def login(phone: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = crud_user.get_by_phone(db, phone)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect phone or password")
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

# POST для получения токена OAuth2 (если нужно)
@router.post("/token")
def login_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
