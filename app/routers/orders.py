from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from app.schemas.order import Order, OrderCreate
from app.services import order_services

router = APIRouter()

@router.post("/", response_model=Order) # Changed response_model to Order for consistency
def create_order(order: OrderCreate):
    try:
        return order_services.create_new_order(order)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[Order])
def read_orders(status: Optional[str] = None):
    """
    Handles both 'GET /orders/' (all) and 'GET /orders/?status=...' (filtered)
    """
    try:
        return order_services.get_all_orders(status=status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{order_id}", response_model=Order)
def read_order(order_id: str):
    order = order_services.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/{order_id}/status")
def update_status(order_id: str, new_status: str):
    try:
        return order_services.update_order_status(order_id, new_status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{order_id}")
def delete_order(order_id: str):
    try:
        order_services.delete_order(order_id)
        return {"detail": "Order deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))