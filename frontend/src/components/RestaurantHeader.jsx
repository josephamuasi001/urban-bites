function MenuItemCard({ item }) {

    return (

        <div className="menu-item-card">

            <img
                src={
                    item.image_url !== "n/a"
                        ? item.image_url
                        : "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=800"
                }
                alt={item.name}
            />

            <div className="menu-item-content">

                <h3>{item.name}</h3>

                <p>{item.description}</p>

                <span className="category">

                    {item.category}

                </span>

                <div className="menu-footer">

                    <strong>

                        GH₵ {item.price}

                    </strong>

                    <button
                        className="btn btn-primary"
                    >
                        Add to Cart
                    </button>

                </div>

            </div>

        </div>

    );

}

export default MenuItemCard;