import './App.css';

function Ex2() {
  return (
    <div>
      <h2>Example 2: Components and Props</h2>
      <div className="App">
        <Job salary="29,000" position="Junior SDE" company="Amazon"/>
        <Job salary="35,000" position="SDE" company="Google"/>
        <Job salary="50,000" position="Senior SDE"/>
      </div><hr/>
    </div>
  );
}


const Job = (props) => {
  return (
    <div>
      <h2>{props.salary}</h2>
      <h3>{props.position}</h3>
      <h3>{props.company}</h3>
      <hr/>
    </div>
  );
}


export default Ex2;

