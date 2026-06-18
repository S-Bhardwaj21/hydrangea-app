from fastapi import Depends, HTTPException, status
from app.database import supabase

async def get_current_user_role(token: str = Depends(...)): # Simplified for structure
    # In a real app, we would verify the JWT with Supabase
    user = supabase.auth.get_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # Return the user's metadata/role defined in your Supabase 'profiles' table
    return user.user.user_metadata.get("role")