import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import RestaurantHeader from "../components/RestaurantHeader";
import MenuSection from "../components/MenuSection";

import { getRestaurant } from "../services/restaurantService";
import { getRestaurantMenu } from "../services/menuService";

function RestaurantDetailsPage() {

    const { id } = useParams();

    const [restaurant, setRestaurant] = useState(null);
    const [menu, setMenu] = useState([]);

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {

        async function loadRestaurant() {

            try {

                const restaurantData = await getRestaurant(id);
                const menuData = await getRestaurantMenu(id);

                setRestaurant(restaurantData);
                setMenu(menuData);

            } catch (err) {

                setError(err.message);

            } finally {

                setLoading(false);

            }

        }

        loadRestaurant();

    }, [id]);

    if (loading) {

        return (
            <div className="container">
                <h2>Loading...</h2>
            </div>
        );

    }

    if (error) {

        return (
            <div className="container">
                <h2>{error}</h2>
            </div>
        );

    }

    return (

        <>
            <RestaurantHeader restaurant={restaurant} />

            <div className="container">
                <MenuSection menu={menu} />
            </div>
        </>

    );

}

export default RestaurantDetailsPage;