import sqlite3
from fastapi import FastAPI, HTTPException, Form

todo_dict = {}

app = FastAPI()

@app.get("/")
def read_root():
    return {"Remembrall": "Gran knows I forget things — this tells you if there's something you've forgotten to do. Look, I've forgotten something already!"}

@app.get("/todo")
def read_root():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    todo_dict = {}
    for index, row in enumerate(rows):
        todo_dict[index] = {"ID": row[0], "Title": row[1], "Description": row[2], "Time": row[3], "Status": row[4]}
    return todo_dict

@app.post("/todo")
def create_todo(ID: str = Form(None), Title: str = Form(None), Description: str = Form(None), Time: str = Form(None), Status: str = Form(None)):
    
    if ID is None:
        raise HTTPException(status_code=400, detail="ID cannot be empty")
    if Title is None:
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    if Description is None:
        raise HTTPException(status_code=400, detail="Description cannot be empty")
    if Time is None:
        raise HTTPException(status_code=400, detail="Time cannot be empty")
    if Status is None:
        raise HTTPException(status_code=400, detail="Status cannot be empty")
    
    ID = int(ID)
    Status = int(Status)

    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?)", (ID, Title, Description, Time, Status))
    conn.commit()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    todo_dict = {}
    for index, row in enumerate(rows):
        todo_dict[index] = {"ID": row[0], "Title": row[1], "Description": row[2], "Time": row[3], "Status": row[4]}
    return todo_dict

@app.delete("/todo/{ID}")
def delete_todo(ID: int = None):
    if ID is None:
        raise HTTPException(status_code=400, detail="ID cannot be empty")
    print(ID)
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE ID=?", (ID,))
    conn.commit()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    todo_dict = {}
    for index, row in enumerate(rows):
        todo_dict[index] = {"ID": row[0], "Title": row[1], "Description": row[2], "Time": row[3], "Status": row[4]}
    return todo_dict


@app.put("/todo/{ID}")
def update_todo(ID, Title: str = Form(None), Description: str = Form(None), Time: str = Form(None), Status: str = Form(None)):
    if ID is None:
        raise HTTPException(status_code=400, detail="ID cannot be empty")
    if Title is None:
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    if Description is None:
        raise HTTPException(status_code=400, detail="Description cannot be empty")
    if Time is None:
        raise HTTPException(status_code=400, detail="Time cannot be empty")
    if Status is None:
        raise HTTPException(status_code=400, detail="Status cannot be empty")
    
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET Title=?, Description=?, Time=?, Status=? WHERE ID=?", (Title, Description, Time, Status, ID))
    conn.commit()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    todo_dict = {}
    for index, row in enumerate(rows):
        todo_dict[index] = {"ID": row[0], "Title": row[1], "Description": row[2], "Time": row[3], "Status": row[4]}
    return todo_dict