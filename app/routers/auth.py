from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import get_user_by_email, create_user, verify_password
from app.services.auth_service import check_user_exists

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/check-email")
def check_email(email: str):
    # This endpoint is for your "smart" frontend check
    # Returns true if user exists, false if new
    db = next(get_db())
    exists = check_user_exists(db, email)
    return {"exists": exists}

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}