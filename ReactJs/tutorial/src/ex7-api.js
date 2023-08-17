import "./App.css"
import Axios from "axios";
import {useState, useEffect} from "react";

function Ex7() {
    
    const [catFact, setCatFact] = useState("");

    const fetchCatFact = async () => {
        const res = await Axios.get("https://catfact.ninja/fact");
        return setCatFact(res.data.fact);
    }

    const [predictedAge, setPredictedAge] = useState(null);
    const [name, setName] = useState("Kyle");

    const fetchAgeData = async () => {
        const res = await Axios.get(`https://api.agify.io/?name=${name}`);
        return setPredictedAge(res.data);
    }

    const [excuse, setExcuse] = useState("");

    const fetchExcuseData = async (excuseType) => {
        const res = await Axios.get(`https://excuser-three.vercel.app/v1/excuse/${excuseType}/`);
        setExcuse(res.data[0].excuse)
    }

    useEffect(() => {    // not needed yet
        fetchCatFact();
        fetchAgeData("Kyle");
        fetchExcuseData("party");
    }, []);
    return (
        <div>
            <h2>Chapter 7 APIs</h2>
            <div className="App">
                <h3>Cat Fact</h3>
                <button onClick={fetchCatFact}>Generate Fact</button>
                <p>{catFact}</p>
            </div>
        
            <div className="App">
                <h3>Age predictor</h3>
                <input onChange={(event)=>{setName(event.target.value)}} placeholder="Enter a Name to predict"></input>
                <button onClick={fetchAgeData}>Submit</button>
                <h3>Age: {predictedAge?.age} | Name: {predictedAge?.name}</h3>
            </div>

            <div className="App">
                <h3>Generate Excuses</h3>

                <div style={{display:"inline", margin:"auto"} }>
                    <button onClick={()=>fetchExcuseData("family")}>Family</button>
                    <button onClick={()=>fetchExcuseData("office")}>Office</button>
                    <button onClick={()=>fetchExcuseData("college")}>College</button>
                    <button onClick={()=>fetchExcuseData("gaming")}>Gaming</button>
                </div>

                <p>{excuse}</p>
            </div>

            <hr/>
        </div>
    );
}

export default Ex7;