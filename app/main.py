from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the auth router
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Hydrangea App"}