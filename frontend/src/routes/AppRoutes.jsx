import { Routes, Route } from "react-router-dom";

function HomePage() {
  return <h1>Home Page</h1>;
}

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
    </Routes>
  );
}

export default AppRoutes;