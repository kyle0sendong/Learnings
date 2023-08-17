import { useEffect, useState } from "react";

export const Text = (props) => {

    const [text, setText] = useState("")

    useEffect( ()=> {
        console.log("Component Mounted");

        return () => {
            // used for cleanups
            console.log("Component Unmounted");
        };

    }, []); // put empty array as 2nd argument on useEffect to only trigger once
    
    const inputText = (
        <div>
            <p>LifeCycle Text</p>
            <input onChange={(event) => {setText(event.target.value)}} placeholder="Input Text Here"></input>
            <p>{text}</p>
        </div>);
    return (
        <div>
            {props.showText && inputText}
        </div>
    );
}