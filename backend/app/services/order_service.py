from app.database.supabase import supabase


def create_order(order, user_id):

    total = 0
    order_items = []

    # Calculate total
    for item in order.items:

        menu = (
            supabase.table("menu_items")
            .select("*")
            .eq("id", item.menu_item_id)
            .execute()
        )

        if not menu.data:
            return {
                "success": False,
                "message": "Menu item not found."
            }

        menu_item = menu.data[0]

        subtotal = menu_item["price"] * item.quantity

        total += subtotal

        order_items.append({
            "menu_item_id": item.menu_item_id,
            "quantity": item.quantity,
            "price": menu_item["price"]
        })

    # Create Order
    new_order = (
        supabase.table("orders")
        .insert({
            "user_id": user_id,
            "restaurant_id": order.restaurant_id,
            "total_amount": total
        })
        .execute()
    )

    order_id = new_order.data[0]["id"]

    # Create Order Items
    for item in order_items:

        supabase.table("order_items").insert({
            "order_id": order_id,
            "menu_item_id": item["menu_item_id"],
            "quantity": item["quantity"],
            "price": item["price"]
        }).execute()

    return {
        "success": True,
        "message": "Order created successfully.",
        "order_id": order_id,
        "total": total
    }


def get_all_orders():

    response = (
        supabase.table("orders")
        .select("*")
        .execute()
    )

    return response.data


def get_my_orders(user_id):

    response = (
        supabase.table("orders")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    return response.data