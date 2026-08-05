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

def update_order_status(order_id, status):

    response = (
        supabase.table("orders")
        .update({
            "status": status
        })
        .eq("id", order_id)
        .execute()
    )

    if not response.data:
        return {
            "success": False,
            "message": "Order not found."
        }

    return {
        "success": True,
        "message": "Order updated successfully.",
        "data": response.data
    }
    

def get_order_by_id(order_id):

    response = (
        supabase.table("orders")
        .select("*")
        .eq("id", order_id)
        .execute()
    )

    if not response.data:
        return {
            "success": False,
            "message": "Order not found."
        }

    return response.data[0]


def delete_order(order_id):

    # Delete order items first
    supabase.table("order_items") \
        .delete() \
        .eq("order_id", order_id) \
        .execute()

    # Delete the order
    response = (
        supabase.table("orders")
        .delete()
        .eq("id", order_id)
        .execute()
    )

    return {
        "success": True,
        "message": "Order deleted successfully.",
        "data": response.data
    }
    
    