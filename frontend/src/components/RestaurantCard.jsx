function RestaurantCard({ restaurant }) {
  return (
    <div className="restaurant-card">

      <div className="restaurant-image">

        <img
          src={restaurant.image}
          alt={restaurant.name}
        />

        <button className="favorite-btn">
          🤍
        </button>

        <div className="rating-badge">
          ⭐ {restaurant.rating}
        </div>

      </div>

      <div className="restaurant-body">

        <h3>{restaurant.name}</h3>

        <div className="restaurant-meta">

          <span>🍔 {restaurant.cuisine}</span>

          <span>🕒 {restaurant.time}</span>

        </div>

        <button className="btn btn-primary restaurant-btn">
          Order Now
        </button>

      </div>

    </div>
  );
}

export default RestaurantCard;