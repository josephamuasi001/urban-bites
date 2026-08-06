import { API_URL } from "../config";

export async function getRestaurants() {
    const response = await fetch(`${API_URL}/restaurants`);

    if (!response.ok) {
        throw new Error("Failed to fetch restaurants.");
    }

    return await response.json();
}

export async function getRestaurant(id) {
    const response = await fetch(`${API_URL}/restaurants/${id}`);

    if (!response.ok) {
        throw new Error("Restaurant not found.");
    }

    return await response.json();
}