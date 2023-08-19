import "./App.css"
import { useState } from "react";

// hook - function that start with use

function Ex4() {
    
    const [age, setAge] = useState(0);
    const increaseAge = () => {
        setAge(age + 1);
    }

    const [inputValue, setInputValue] = useState("")
    
    const handleInputChange = (event) => {
        setInputValue(event.target.value);
    }

    const [showText, setShowText] = useState(true);

    const[value, setValue] = useState(0);

    const increaseValue = () => {
        setValue(value+1)
    }

    const decreaseValue = () => {
        setValue(value-1)
    }

    const setValueToZero = () => {
        setValue(0)
    }

    return(
        <div>
            <h2>Chapter 4 - States</h2>
            <div className="App">
                <p>{age}</p>
                <button onClick={increaseAge}>Increase Age!</button>

                <div>
                    <input type="text" onChange={handleInputChange} placeholder="Type text here!"></input>
                    <p>{inputValue}</p>
                </div>

                <div>
                    <button onClick={ () => {setShowText(!showText)}}>Show/Hide Text</button>
                    {showText === true && <h3>Hello Hidden Text</h3>}
                </div>

            </div>

            <h3>Chapter 4 exercise</h3>
            <div className="App">
                <h3>{value}</h3>
                <button onClick={increaseValue}>Increase</button>
                <button onClick={decreaseValue}>Decrease</button>
                <button onClick={setValueToZero}>Set Zero</button>
            </div>
            <hr/>
        </div>
    );
}

export default Ex4;