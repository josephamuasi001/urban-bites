from app.database.supabase import supabase
from app.security.hashing import hash_password, verify_password
from app.auth.jwt_handler import create_access_token

def create_user(user):

    # Check if email already exists
    existing = (
        supabase.table("users")
        .select("*")
        .eq("email", user.email)
        .execute()
    )

    if existing.data:
        return {
            "success": False,
            "message": "Email already exists."
        }

    hashed_password = hash_password(user.password)

    response = (
        supabase.table("users")
        .insert({
            "full_name": user.full_name,
            "email": user.email,
            "password_hash": hashed_password,
            "phone": user.phone
        })
        .execute()
    )

    return {
        "success": True,
        "message": "User registered successfully.",
        "data": response.data
    }
    
    

def get_all_users():

    response = (
        supabase.table("users")
        .select("id, full_name, email, phone, created_at")
        .execute()
    )

    return response.data


def login_user(user):

    response = (
        supabase.table("users")
        .select("*")
        .eq("email", user.email)
        .execute()
    )

    if not response.data:
        return {
            "success": False,
            "message": "Invalid email or password."
        }

    db_user = response.data[0]

    if not verify_password(user.password, db_user["password_hash"]):
        return {
            "success": False,
            "message": "Invalid email or password."
        }

    token = create_access_token(
        {
            "sub": db_user["id"],
            "email": db_user["email"]
        }
    )

    return {
        "success": True,
        "access_token": token,
        "token_type": "bearer"
    }