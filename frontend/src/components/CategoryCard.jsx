function CategoryCard({ image, name }) {
  return (
    <div className="category-card">
      <img src={image} alt={name} />

      <h3>{name}</h3>
    </div>
  );
}

export default CategoryCard;