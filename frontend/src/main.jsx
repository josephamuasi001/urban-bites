import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import "./index.css";

import "./styles/variables.css";
import "./styles/globals.css";
import "./styles/navbar.css";
import "./styles/footer.css";
import "./styles/buttons.css";
import "./styles/cards.css";
import "./styles/homepage.css";

import App from "./App";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>
);