from app.database.supabase import supabase

from app.database.supabase import supabase


def create_order_item(order_item):

    response = (
        supabase.table("order_items")
        .insert({
            "order_id": order_item.order_id,
            "menu_item_id": order_item.menu_item_id,
            "quantity": order_item.quantity,
            "price": order_item.price
        })
        .execute()
    )
    update_order_total(order_item.order_id)

    return {
        "success": True,
        "message": "Order item added successfully.",
        "data": response.data
    }


def get_all_order_items():

    response = (
        supabase.table("order_items")
        .select("*")
        .execute()
    )

    return response.data


def get_order_item_by_id(order_item_id):

    response = (
        supabase.table("order_items")
        .select("*")
        .eq("id", order_item_id)
        .execute()
    )

    if not response.data:
        return {
            "success": False,
            "message": "Order item not found."
        }

    return response.data[0]


def update_order_total(order_id):

    # Get all items for this order
    response = (
        supabase.table("order_items")
        .select("price")
        .eq("order_id", order_id)
        .execute()
    )

    total = 0

    for item in response.data:
        total += float(item["price"])

    # Update orders table
    (
        supabase.table("orders")
        .update({
            "total_amount": total
        })
        .eq("id", order_id)
        .execute()
    )

    return total