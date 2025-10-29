from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

app = FastAPI(title="Todo App Backend")

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo-service:27017/')
client = AsyncIOMotorClient(MONGO_URI)
db = client.todo_db
todos = db.todos

class Todo(BaseModel):
    title: str
    description: str = ''
    completed: bool = False

def out(doc):
    doc['id'] = str(doc['_id'])
    doc.pop('_id', None)
    return doc

@app.post('/todos/', status_code=201)
async def create_todo(todo: Todo):
    res = await todos.insert_one(todo.dict())
    doc = await todos.find_one({'_id': res.inserted_id})
    return out(doc)

@app.get('/todos/')
async def list_todos():
    items = []
    cursor = todos.find()
    async for doc in cursor:
        items.append(out(doc))
    return items

@app.get('/todos/{todo_id}')
async def get_todo(todo_id: str):
    doc = await todos.find_one({'_id': ObjectId(todo_id)})
    if not doc:
        raise HTTPException(status_code=404, detail='Not found')
    return out(doc)

@app.put('/todos/{todo_id}')
async def update_todo(todo_id: str, todo: Todo):
    res = await todos.update_one({'_id': ObjectId(todo_id)}, {'$set': todo.dict()})
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    doc = await todos.find_one({'_id': ObjectId(todo_id)})
    return out(doc)

@app.patch('/todos/{todo_id}')
async def patch_todo(todo_id: str, payload: dict):
    res = await todos.update_one({'_id': ObjectId(todo_id)}, {'$set': payload})
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    doc = await todos.find_one({'_id': ObjectId(todo_id)})
    return out(doc)

@app.delete('/todos/{todo_id}')
async def delete_todo(todo_id: str):
    res = await todos.delete_one({'_id': ObjectId(todo_id)})
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Not found')
    return {'message': 'deleted'}
