import CategoryCard from "./CategoryCard";

const categories = [
  {
    name: "Burgers",
    image: "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=300"
  },
  {
    name: "Pizza",
    image: "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=300"
  },
  {
    name: "Chicken",
    image: "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?w=300"
  },
  {
    name: "Mexican",
    image: "https://images.unsplash.com/photo-1613514785940-daed07799d9b?w=300"
  },
  {
    name: "Salads",
    image: "https://images.unsplash.com/photo-1546793665-c74683f339c1?w=300"
  },
  {
    name: "Desserts",
    image: "https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?w=300"
  },
  {
    name: "Drinks",
    image: "https://images.unsplash.com/photo-1544145945-f90425340c7e?w=300"
  },
  {
    name: "Noodles",
    image: "https://images.unsplash.com/photo-1617093727343-374698b1b08d?w=300"
  }
];

function Categories() {
  return (
    <section className="categories">

      <div className="container">

        <h2 className="section-title">
          Browse by Category
        </h2>

        <div className="category-grid">

          {categories.map((category) => (
            <CategoryCard
              key={category.name}
              image={category.image}
              name={category.name}
            />
          ))}

        </div>

      </div>

    </section>
  );
}

export default Categories;