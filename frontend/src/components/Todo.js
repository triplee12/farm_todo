import React from "react";
import axios from "axios";

function TodoItem(props) {
    const DeleteTodoHandler = (title) => {
        axios.delete(`http://127.0.0.1:8000/api/todos/delete/${title}`).then(res => console.log(res.data));
    }
    return (
        <div>
            <p>
                <span style={{ "fontWeight": "bold, underline" }}>
                    {props.todo.title}:
                </span>
                {props.todo.description}
                <button onClick={() => DeleteTodoHandler(props.todo.title)} className="btn btn-outline-danger my-2 mx-2" style={{"borderRadius": "50px",}}>X</button>
            </p>
            <hr></hr>
        </div>
    );
}

export default TodoItem;
