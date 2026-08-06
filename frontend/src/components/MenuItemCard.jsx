function MenuItemCard({ item }) {
  return (
    <div className="food-card">
      <img
        src={
          item.image_url !== "n/a"
            ? item.image_url
            : "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800"
        }
        alt={item.name}
      />

      <div className="food-card-body">
        <h3>{item.name}</h3>

        <p>{item.description}</p>

        <div className="food-card-footer">
          <strong>GH₵ {item.price}</strong>

          <button className="btn btn-primary">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
}

export default MenuItemCard;