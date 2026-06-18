from fastapi import FastAPI
from app.routers import orders # Import your router

app = FastAPI(title="Hydrangea API")

# Include the router
app.include_router(orders.router, prefix="/orders", tags=["orders"])

@app.get("/")
def read_root():
    return {"message": "Hydrangea API is operational"}