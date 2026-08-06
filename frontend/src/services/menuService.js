import { API_URL } from "../config";

export async function getRestaurantMenu(restaurantId) {

    const response = await fetch(
        `${API_URL}/menus/${restaurantId}`
    );

    if (!response.ok) {
        throw new Error("Failed to fetch menu.");
    }

    return await response.json();

}

