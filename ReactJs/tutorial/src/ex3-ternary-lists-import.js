import './App.css';
import {User} from './User.js'
import { GasPlanet } from './Planets';

function Ex3() {
  const age = 20
  let isRed = true

  const users = [
    {name:"A", age:112323},
    {name:"B", age:39}
  ]
  
  const planets = [
    {name: "Mars", isGasPlanet: false},
    {name: "Earth", isGasPlanet: false},
    {name: "Jupiter", isGasPlanet: true},
    {name: "Venus", isGasPlanet: false},
    {name: "Saturn", isGasPlanet: true},
    {name: "Neptune", isGasPlanet: true},
    {name: "Uranus", isGasPlanet: true},
  ]

  return (
    <div>
      <h2>Example 3: </h2>
      <div className="App">
        <h1>{age > 33 ? "asd" : 12 }</h1>
        <h1 style={{color: isRed ? "red" : "green"}}>asd</h1>
        {isRed && <button>Nice button</button>}
        <p>List Mapping:</p>
        <ListMapping user={users}/>


      </div>

      <h2>Exercise: <b>Gas Planets</b></h2>
      <div className="App">
        <GasPlanet planets={planets}/>
      </div>
      <hr/>
    </div>


  );
}


const ListMapping = (props) => {
  return (
    <div>
      {props.user.map(
        (user, key) => {
          return <User name={user.name} age={user.age} />
        }
      )}
    </div>
  );
}


export default Ex3;

