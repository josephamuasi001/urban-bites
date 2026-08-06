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

    return (

        <>
            <Navbar />

            <main className="container">

                <section className="page-header">

                    <span className="section-label">
                        DISCOVER
                    </span>

                    <h1>Restaurants</h1>

                    <p>
                        Discover amazing restaurants around you.
                    </p>

                </section>

                {loading && <h2>Loading restaurants...</h2>}

                {error && <h2>{error}</h2>}

                <div className="restaurant-grid">

                    {restaurants.map((restaurant) => (

                        <RestaurantCard
                            key={restaurant.id}
                            restaurant={restaurant}
                        />

                    ))}

                </div>

            </main>

            <Footer />
        </>

    );

}

export default RestaurantsPage;