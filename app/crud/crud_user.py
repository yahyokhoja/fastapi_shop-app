from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

class CRUDUser:
    def get(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_by_phone(self, db: Session, phone: str):
        return db.query(User).filter(User.phone == phone).first()

    def create(self, db: Session, user: UserCreate):
        db_user = User(
            phone=user.phone,
            hashed_password=get_password_hash(user.password),
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

crud_user = CRUDUser()
