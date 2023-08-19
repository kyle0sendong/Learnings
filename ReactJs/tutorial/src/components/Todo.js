export const Todo = (props) => {
    return (
        <div style={{display:"flex", justifyContent:"center"}}>
            <p style={{backgroundColor: props.complete === true && "yellow", width:"100px"}}> {props.todoName} </p>
            <button style={{height:"40px", margin:"10px"}}onClick={() => props.completeTodo(props.id)}> Complete </button>
            <button style={{height:"40px", margin:"10px"}}onClick={() => props.deleteTodo(props.id)}> x </button>
        </div>
    );
};