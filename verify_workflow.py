from app.services.order_services import create_new_order, update_order_status, delete_order
from app.schemas.order import OrderCreate

def dry_run():
    print("--- Starting Dry Run ---")
    
    # 1. Create a DRAFT order
    order = create_new_order(OrderCreate(user_id="test_user", material_description="Silk", target_date="2026-07-01"))
    order_id = order[0]['id']
    print(f"Created DRAFT Order: {order_id}")

    # 2. Test Invalid Transition (Guardrail Check)
    try:
        print("Attempting illegal transition: DRAFT -> SHIPPED...")
        update_order_status(order_id, "shipped")
    except Exception as e:
        print(f"Success! Guardrail worked: {e}")

    # 3. Test Valid Transition
    print("Transitioning to: pending_quote...")
    update_order_status(order_id, "pending_quote")
    print("Transition successful.")

    # 4. Cleanup
    print("Attempting to delete (should fail now that it's not DRAFT)...")
    try:
        delete_order(order_id)
    except Exception as e:
        print(f"Success! Guardrail blocked deletion: {e}")
        print("--- Dry Run Complete ---")

if __name__ == "__main__":
    dry_run()