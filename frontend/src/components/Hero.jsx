
import SearchBar from "./SearchBar";
import StatCard from "./StatCard";
function Hero() {
  return (
    <section className="hero">
      <div className="hero-text">

    <span className="hero-badge">
        🍔 Fast Delivery
    </span>

    <h1>
        Delicious Food,
        <br />
        Delivered Fast
    </h1>

    <p>
        Discover the best restaurants around you
        and enjoy fresh meals delivered straight
        to your door.
    </p>

    <SearchBar />

    <div className="hero-actions">

        <button className="btn btn-primary">
            Order Now
        </button>

        <button className="btn btn-outline">
            Browse Menu
        </button>

    </div>

    <div className="hero-stats">

        <StatCard
            number="500+"
            text="Restaurants"
        />

        <StatCard
            number="50K+"
            text="Happy Customers"
        />

        <StatCard
            number="30 Min"
            text="Average Delivery"
        />

    </div>

</div>
    </section>
  );
}

export default Hero;