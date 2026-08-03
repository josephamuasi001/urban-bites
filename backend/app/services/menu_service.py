from app.database.supabase import supabase


def create_menu_item(menu_item):

    response = (
        supabase.table("menu_items")
        .insert({
            "restaurant_id": menu_item.restaurant_id,
            "name": menu_item.name,
            "description": menu_item.description,
            "category": menu_item.category,
            "price": menu_item.price,
            "image_url": menu_item.image_url,
            "is_available": menu_item.is_available
        })
        .execute()
    )

    return {
        "success": True,
        "message": "Menu item created successfully.",
        "data": response.data
    }


def get_all_menu_items():

    response = (
        supabase.table("menu_items")
        .select("*")
        .execute()
    )

    return response.data


def get_menu_items_by_restaurant(restaurant_id):

    response = (
        supabase.table("menu_items")
        .select("*")
        .eq("restaurant_id", restaurant_id)
        .execute()
    )

    return response.data