import "./App.css";
import {BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";
import { NavBar } from "./components/Navbar";
import { Home } from "./pages/Home";
import { Menu } from "./pages/Menu";
import { Contacts } from "./pages/Contacts";

function Ex8() {

    return (
        <div>
            <h3>Chapter 8: React Router</h3>

            <Router>
                <NavBar />

                <Routes>
                    <Route path="/home" element={<Home />}/>
                    <Route path="/menu" element={<Menu />}/>
                    <Route path="/contacts" element={<Contacts />}/>
                    <Route path="*" element={<h2>PAGE NOT FOUND</h2>} />
                </Routes>
            </Router>

        </div>
    );
}

export default Ex8;