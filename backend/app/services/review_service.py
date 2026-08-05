from app.database.supabase import supabase


def create_review(review, user_id):

    response = (
        supabase.table("reviews")
        .insert({
            "user_id": user_id,
            "restaurant_id": review.restaurant_id,
            "rating": review.rating,
            "comment": review.comment
        })
        .execute()
    )

    return {
        "success": True,
        "message": "Review submitted successfully.",
        "data": response.data
    }


def get_restaurant_reviews(restaurant_id):

    response = (
        supabase.table("reviews")
        .select("*")
        .eq("restaurant_id", restaurant_id)
        .execute()
    )

    return response.data


def get_review_by_id(review_id):

    response = (
        supabase.table("reviews")
        .select("*")
        .eq("id", review_id)
        .execute()
    )

    if not response.data:
        return {
            "success": False,
            "message": "Review not found."
        }

    return response.data[0]


def update_review(review_id, review):

    response = (
        supabase.table("reviews")
        .update({
            "restaurant_id": review.restaurant_id,
            "rating": review.rating,
            "comment": review.comment
        })
        .eq("id", review_id)
        .execute()
    )

    if not response.data:
        return {
            "success": False,
            "message": "Review not found."
        }

    return {
        "success": True,
        "message": "Review updated successfully.",
        "data": response.data
    }
    

def delete_review(review_id):

    response = (
        supabase.table("reviews")
        .delete()
        .eq("id", review_id)
        .execute()
    )

    return {
        "success": True,
        "message": "Review deleted successfully.",
        "data": response.data
    }

