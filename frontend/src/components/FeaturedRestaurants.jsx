import RestaurantCard from "./RestaurantCard";

const restaurants = [
  {
    id: 1,
    name: "Burger Hub",
    cuisine: "Fast Food",
    rating: 4.7,
    time: "25 mins",
    image:
      "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=700",
  },

  {
    id: 2,
    name: "Pizza Palace",
    cuisine: "Italian",
    rating: 4.8,
    time: "30 mins",
    image:
      "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=700",
  },

  {
    id: 3,
    name: "Sushi World",
    cuisine: "Japanese",
    rating: 4.9,
    time: "20 mins",
    image:
      "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=700",
  },
];

function FeaturedRestaurants() {
  return (
    <section className="featured section">

      <div className="section-header">

        <div>

          <span className="section-label">
            FEATURED
          </span>

          <h2>Featured Restaurants</h2>

          <p>
            Discover our most popular restaurants near you.
          </p>

        </div>

        <button className="btn btn-outline">
          View All
        </button>

      </div>

      <div className="restaurant-grid">

        {restaurants.map((restaurant) => (
          <RestaurantCard
            key={restaurant.id}
            restaurant={restaurant}
          />
        ))}

      </div>

    </section>
  );
}

export default FeaturedRestaurants;