import Hero from "../components/Hero";
import Categories from "../components/Categories"
import FeaturedRestaurants from "../components/FeaturedRestaurants";
import PopularDishes from "../components/PopularDishes";
import Footer from "../components/Footer";


function HomePage() {
  return (
    <>
      <Hero />
      <Categories />
      <FeaturedRestaurants />
      <PopularDishes />  
          
    </>
  );
}

export default HomePage;