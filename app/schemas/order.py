from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class OrderStatus(str, Enum):
    DRAFT = "draft"
    PENDING_QUOTE = "pending_quote"
    AWAITING_PAYMENT = "awaiting_payment"
    IN_PRODUCTION = "in_production"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

class Order(BaseModel):
    id: Optional[str] = None
    status: str = "DRAFT"
    client_name: str
    contact_number: str
    priority_level: str = "NORMAL"  # NORMAL, URGENT
    measurement_notes: Optional[str] = None
    material_details: Optional[str] = None
    
class OrderBase(BaseModel):
    user_id: str
    material_description: str
    target_date: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: str
    status: OrderStatus = OrderStatus.DRAFT
    boutique_id: Optional[str] = None
    price: Optional[float] = None

    class Config:
        from_attributes = True