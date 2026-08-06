import { Link } from "react-router-dom";

function RestaurantCard({ restaurant }) {

  return (
    
    <div className="restaurant-card">

      <div className="restaurant-image">

        <img
          src={
            restaurant.image_url !== "n/a"
              ? restaurant.image_url
              : "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800"
          }
          alt={restaurant.name}
        />

        <div className="rating-badge">
          ⭐ {restaurant.rating}
        </div>

      </div>

      <div className="restaurant-body">

        <h3>{restaurant.name}</h3>

        <p>{restaurant.cuisine}</p>

        <div className="restaurant-meta">

          <span>📍 {restaurant.city}</span>

          <span>
            🕒 {restaurant.opening_time} - {restaurant.closing_time}
          </span>

        </div>

        <div className="restaurant-meta">

          <span>🚚 GH₵ {restaurant.delivery_fee}</span>

          <span>
            {restaurant.is_open ? "🟢 Open" : "🔴 Closed"}
          </span>

        </div>

        <Link
          to={`/restaurants/${restaurant.id}`}
          className="btn btn-primary restaurant-btn"
        >
          View Restaurant
        </Link>

      </div>

    </div>
  );
}



export default RestaurantCard;