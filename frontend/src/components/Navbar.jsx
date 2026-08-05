import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "20px 50px",
        borderBottom: "1px solid #ddd",
      }}
    >
      <h2>🍔 Urban Bite</h2>

      <div
        style={{
          display: "flex",
          gap: "20px",
        }}
      >
        <Link to="/">Home</Link>

        <Link to="/restaurants">Restaurants</Link>

        <Link to="/cart">Cart</Link>

        <Link to="/orders">Orders</Link>

        <Link to="/profile">Profile</Link>
      </div>
    </nav>
  );
}

export default Navbar;