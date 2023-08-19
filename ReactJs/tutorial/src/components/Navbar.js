import "../App.css";
import { Link } from "react-router-dom";

export const NavBar = () => {
    return (
        <div className="App">
            <Link to="/home">Home</Link>
            <Link to="/menu">Menu</Link>
            <Link to="/contacts">Contacts</Link>
        </div>
    );
}