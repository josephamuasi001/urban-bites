function FoodCard({ food }) {
  return (
    <div className="food-card">

      <div className="food-image">

        <img
          src={food.image}
          alt={food.name}
        />

        <button className="favorite-btn">
          🤍
        </button>

      </div>

      <div className="food-body">

        <h3>{food.name}</h3>

        <small>{food.restaurant}</small>

        <div className="food-rating">
          ⭐ {food.rating}
        </div>

        <div className="food-footer">

          <span className="food-price">
            GH₵ {food.price}
          </span>

          <button className="add-btn">
            +
          </button>

        </div>

      </div>

    </div>
  );
}

export default FoodCard;