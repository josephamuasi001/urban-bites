import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import RestaurantCard from "../components/RestaurantCard";
import Footer from "../components/Footer";

import { getRestaurants } from "../services/restaurantService";

function RestaurantsPage() {

    const [restaurants, setRestaurants] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {

        async function fetchRestaurants() {

            try {

                const data = await getRestaurants();

                setRestaurants(data);

            } catch (err) {

                setError(err.message);

            } finally {

                setLoading(false);

            }

        }

        fetchRestaurants();

    }, []);

    return 

}

export default RestaurantsPage;