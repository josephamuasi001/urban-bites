import { FiSearch } from "react-icons/fi";

function SearchBar() {
  return (
    <div className="search-bar">

      <input
        type="text"
        placeholder="Search restaurants or meals..."
      />

      <FiSearch className="search-icon" />

    </div>
  );
}

export default SearchBar;