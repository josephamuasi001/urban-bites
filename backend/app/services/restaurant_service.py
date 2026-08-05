from app.database.supabase import supabase


def create_restaurant(restaurant):

    existing = (
        supabase.table("restaurants")
        .select("*")
        .eq("email", restaurant.email)
        .execute()
    )

    if existing.data:
        return {
            "success": False,
            "message": "Restaurant already exists."
        }

    response = (
        supabase.table("restaurants")
        .insert({
            "name": restaurant.name,
            "description": restaurant.description,
            "cuisine": restaurant.cuisine,
            "address": restaurant.address,
            "city": restaurant.city,
            "phone": restaurant.phone,
            "email": restaurant.email,
            "image_url": restaurant.image_url,
            "opening_time": restaurant.opening_time,
            "closing_time": restaurant.closing_time,
            "delivery_fee": restaurant.delivery_fee,
            "minimum_order": restaurant.minimum_order
        })
        .execute()
    )

    return {
        "success": True,
        "message": "Restaurant created successfully.",
        "data": response.data
    }


def get_all_restaurants():

    response = (
        supabase.table("restaurants")
        .select("*")
        .execute()
    )

    return response.data


def get_restaurant_by_id(restaurant_id):

    response = (
        supabase.table("restaurants")
        .select("*")
        .eq("id", restaurant_id)
        .execute()
    )

    if not response.data:
        return {
            "success": False,
            "message": "Restaurant not found."
        }

    return response.data[0]


def update_restaurant(restaurant_id, restaurant):

    response = (
        supabase.table("restaurants")
        .update({
            "name": restaurant.name,
            "description": restaurant.description,
            "cuisine": restaurant.cuisine,
            "address": restaurant.address,
            "city": restaurant.city,
            "phone": restaurant.phone,
            "email": restaurant.email,
            "image_url": restaurant.image_url,
            "opening_time": restaurant.opening_time,
            "closing_time": restaurant.closing_time,
            "delivery_fee": restaurant.delivery_fee,
            "minimum_order": restaurant.minimum_order
        })
        .eq("id", restaurant_id)
        .execute()
    )

    return {
        "success": True,
        "message": "Restaurant updated successfully.",
        "data": response.data
    }