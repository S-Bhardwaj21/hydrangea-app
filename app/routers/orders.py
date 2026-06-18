from fastapi import APIRouter, HTTPException
from app.schemas.order import Order, OrderCreate
from app.services import order_services
from app.services.order_services import create_new_order

router = APIRouter()

@router.post("/", response_model=list[Order])
def create_order(order: OrderCreate):
    try:
        # Since we imported the function directly, we use it directly
        return create_new_order(order)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=list[Order])
def read_orders():
    try:
        from app.services.order_services import get_all_orders
        return get_all_orders()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.patch("/{order_id}/status")
def update_status(order_id: str, new_status: str):
    try:
        return order_services.update_order_status(order_id, new_status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))