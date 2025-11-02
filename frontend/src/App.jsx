import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [todos, setTodos] = useState([]);
  const [todo, setTodo] = useState("");

  const backendURL = "http://35.225.48.45:8080";

  useEffect(() => {
    axios.get(`${backendURL}/todo`).then((res) => setTodos(res.data));
  }, []);

  const addTodo = () => {
    axios.post(`${backendURL}/todo`, { title: todo }).then(() => {
      setTodo("");
      axios.get(`${backendURL}/todo`).then((res) => setTodos(res.data));
    });
  };

  const deleteTodo = (id) => {
    axios.delete(`${backendURL}/todo/${id}`).then(() => {
      setTodos(todos.filter((t) => t._id !== id));
    });
  };

  return (
    <div className="app">
      <h1>Todo App</h1>
      <input
        value={todo}
        onChange={(e) => setTodo(e.target.value)}
        placeholder="Add Todo"
      />
      <button onClick={addTodo}>Add</button>

      <ul>
        {todos.map((t) => (
          <li key={t._id}>
            {t.title}
            <button onClick={() => deleteTodo(t._id)}>❌</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
