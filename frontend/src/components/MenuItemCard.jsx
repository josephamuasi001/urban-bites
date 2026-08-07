import { useCart } from "../context/CartContext";

function MenuItemCard({ item }) {
  return (
    <div className="food-card">

      <div className="food-card-image">

        <img
          src={
            item.image_url !== "n/a"
              ? item.image_url
              : "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800"
          }
          alt={item.name}
        />

        {!item.is_available && (
          <span className="food-unavailable">
            Sold Out
          </span>
        )}

      </div>

      <div className="food-card-body">

        <h3>{item.name}</h3>

        <p>{item.description}</p>

        <div className="food-card-footer">

          <strong>
            GH₵ {Number(item.price).toFixed(2)}
          </strong>

          <button
            className="btn btn-primary"
            disabled={!item.is_available}
          >
            {item.is_available ? "Add to Cart" : "Unavailable"}
          </button>

        </div>

      </div>

    </div>
  );
}

export default MenuItemCard;