function SearchBar() {
  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search restaurants or meals..."
      />

      <button className="search-btn">
        🔍
      </button>
    </div>
  );
}

export default SearchBar;