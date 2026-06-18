from app.database import supabase
from app.schemas.order import OrderCreate

def create_new_order(order_data: OrderCreate):
    # .model_dump() converts our Pydantic object to a standard Python dictionary
    # which Supabase expects.
    response = supabase.table("orders").insert(order_data.model_dump()).execute()
    return response.data

def get_all_orders():
    response = supabase.table("orders").select("*").execute()
    return response.data

def update_order_status(order_id: str, new_status: str):
    # Define allowed transitions
    transitions = {
        "draft": ["pending_quote"],
        "pending_quote": ["awaiting_payment"],
        "awaiting_payment": ["in_production"],
        "in_production": ["shipped"],
        "shipped": ["delivered"],
        "delivered": [] # Terminal state
    }

    # 1. Fetch current status
    current_order = supabase.table("orders").select("status").eq("id", order_id).single().execute()
    current_status = current_order.data["status"]

    # 2. Check if transition is allowed
    if new_status not in transitions.get(current_status, []):
        raise Exception(f"Illegal transition from {current_status} to {new_status}")

    # 3. Update the database
    return supabase.table("orders").update({"status": new_status}).eq("id", order_id).execute()

def get_all_orders(status: str = None):
    query = supabase.table("orders").select("*")
    if status:
        query = query.eq("status", status)
    return query.execute().data

def get_order_by_id(order_id: str):
    response = supabase.table("orders").select("*").eq("id", order_id).single().execute()
    return response.data