import { Outlet } from "react-router-dom";

function MainLayout() {
  return (
    <>
      <header>
        <h2>Urban Bite Navbar</h2>
      </header>

      <main>
        <Outlet />
      </main>

      <footer>
        <p>© 2026 Urban Bite</p>
      </footer>
    </>
  );
}

export default MainLayout;