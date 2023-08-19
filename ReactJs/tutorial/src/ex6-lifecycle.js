import { useState } from "react";
import "./App.css";
import {Text} from "./components/Text";

function Ex6() {
    const [showText, setShowText] = useState(false);

    return (
        <div>
            <h2>Chapter 6: Lifecycle</h2>
            <div>
                <button onClick={() => setShowText(!showText)}> Show Text</button>
                <Text showText={showText}/>
            </div> <hr />

        </div> 
    );
}


export default Ex6;