import MenuItemCard from "./MenuItemCard";

function MenuSection({ menu }) {
  return (
    <section className="menu-section">

      <h2>Menu</h2>

      <div className="food-grid">
        {menu.map((item) => (
          <MenuItemCard
            key={item.id}
            item={item}
          />
        ))}
      </div>

    </section>
  );
}

export default MenuSection;