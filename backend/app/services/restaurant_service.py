from app.database.supabase import supabase


def create_restaurant(restaurant):

    response = (
        supabase.table("restaurants")
        .insert({
            "name": restaurant.name,
            "description": restaurant.description,
            "address": restaurant.address,
            "phone": restaurant.phone,
            "email": restaurant.email,
            "image_url": restaurant.image_url,
            "opening_time": restaurant.opening_time,
            "closing_time": restaurant.closing_time,
            "is_open": restaurant.is_open
        })
        .execute()
    )

    return {
        "success": True,
        "message": "Restaurant created successfully.",
        "data": response.data
    }