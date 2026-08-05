import FloatingBadge from "./FloatingBadge";


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
        label="Restaurants"
    />

    <StatCard
        number="50K+"
        label="Happy Customers"
    />

    <StatCard
        number="30 Min"
        label="Average Delivery"
    />

</div>

    <div className="hero-image">

    <img
        src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=700"
        alt="Burger"
    />

    <FloatingBadge
        icon="⭐"
        title="Rating"
        value="4.9"
        className="badge-rating"
    />

    <FloatingBadge
        icon="🚚"
        title="Delivery"
        value="20 Min"
        className="badge-delivery"
    />

    <FloatingBadge
        icon="🔥"
        title="Popular"
        value="500+ Orders"
        className="badge-popular"
    />

</div>
</div>
    </section>
  );
}

export default Hero;