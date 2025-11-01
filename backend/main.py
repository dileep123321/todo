from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection (service name inside cluster)
client = MongoClient("mongodb://mongo-service:27017/")
db = client.todo_db
collection = db.todos

@app.get("/todo")
def get_todos():
    todos = list(collection.find())
    for todo in todos:
        todo["_id"] = str(todo["_id"])
    return todos

@app.post("/todo")
def add_todo(todo: dict):
    result = collection.insert_one(todo)
    todo["_id"] = str(result.inserted_id)
    return todo

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: str):
    result = collection.delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}

