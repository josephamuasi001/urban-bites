import Hero from "../components/Hero";
import Categories from "../components/Categories"
import FeaturedRestaurants from "../components/FeaturedRestaurants";


function HomePage() {
  return (
    <>
      <Hero />
      <Categories />
      <FeaturedRestaurants />
    </>
  );
}

export default HomePage;