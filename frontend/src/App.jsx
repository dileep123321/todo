import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { BACKEND_URL } from './config';

export default function App(){
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState('');

  const load = async () => {
    try{
      const res = await axios.get(`${BACKEND_URL}/todos/`);
      setTodos(res.data);
    }catch(e){ console.error(e); }
  };

  useEffect(()=>{ load(); }, []);

  const add = async () => {
    if(!title) return;
    await axios.post(`${BACKEND_URL}/todos/`, { title, description: '', completed: false });
    setTitle('');
    load();
  };

  const remove = async (id) => {
    await axios.delete(`${BACKEND_URL}/todos/${id}`);
    load();
  };

  const toggle = async (t) => {
    await axios.patch(`${BACKEND_URL}/todos/${t.id}`, { completed: !t.completed });
    load();
  };

  return (
    <div style={{maxWidth:600, margin:'40px auto', padding:20}}>
      <h1>Todo App</h1>
      <div style={{display:'flex', gap:8}}>
        <input value={title} onChange={e=>setTitle(e.target.value)} placeholder="New task" style={{flex:1,padding:8}} />
        <button onClick={add}>Add</button>
      </div>
      <ul>
        {todos.map(t=>(
          <li key={t.id} style={{display:'flex',justifyContent:'space-between',marginTop:10}}>
            <span onClick={()=>toggle(t)} style={{textDecoration:t.completed?'line-through':'none',cursor:'pointer'}}>{t.title}</span>
            <div>
              <button onClick={()=>remove(t.id)} style={{marginLeft:8}}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}
