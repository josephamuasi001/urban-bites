import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">

      <div className="container navbar-container">

        <div className="logo">
          🍔 Urban Bite
        </div>

        <div className="nav-links">

          <Link to="/">Home</Link>

          <Link to="/restaurants">Restaurants</Link>

          <Link to="/cart">Cart</Link>

          <Link to="/orders">Orders</Link>

          <Link to="/profile">Profile</Link>

        </div>

      </div>

    </nav>
  );
}

export default Navbar;