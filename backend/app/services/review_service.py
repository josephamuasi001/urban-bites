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