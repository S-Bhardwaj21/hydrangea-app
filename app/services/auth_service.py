from sqlalchemy.orm import Session
from app.crud.user import get_user_by_email

def check_user_exists(db: Session, email: str):
    user = get_user_by_email(db, email)
    return user is not None