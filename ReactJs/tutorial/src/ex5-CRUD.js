import './App.css';
import {useState} from "react";
import {Todo} from './Todo.js';

function Ex5() {

    const [todoList, setTodoList] = useState([]);
    const [newTodo, setNewTodo] = useState("");

    const addTodo = () => {
        const todo = {
            id: todoList.length === 0 ? 1 : todoList[todoList.length-1].id + 999,
            todoName: newTodo,
            complete: false
        };
        
        setTodoList([...todoList, todo]);
    };

    const deleteTodo = (id) => {
        setTodoList(todoList.filter((todo) => todo.id !== id ));
    };

    const completeTodo = (id) => {
        
        setTodoList(
            todoList.map((todo)=> {
                if (todo.id === id) {
                    return {...todo, complete: true};
                } else {
                    return todo;
                }
            })
        );
    };

    const inputChange = (event) => {
        setNewTodo(event.target.value);
    };

    return (
        <div>

            <h3>Example 5: CRUD - todo list</h3>

            <div> 
                <input type="text" placeholder="Add Todo Here" onChange={inputChange}></input>
                <button onClick={addTodo}>Save</button>
            </div>

            <div className="App">
                {todoList.map((todo) => {
                    return (
                        <Todo
                            todoName={todo.todoName} 
                            id={todo.id}
                            complete={todo.complete}
                            completeTodo={completeTodo}
                            deleteTodo={deleteTodo} />
                    );
                })}
            </div>
        <hr/>
        </div>
    );
}

export default Ex5;
