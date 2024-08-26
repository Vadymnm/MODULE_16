from fastapi import FastAPI, status, Body, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')

users_db = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
async def get_all(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})

@app.get(path="/user/{user_id}")
def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users_db[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}")
async def create_user(user: User) -> str:
    user.id = len(users_db)
    if user.id == 0:
        user.id = 1
    else:
        user.id += 1
    users_db.append(user)
    return f"User № {user.id} is registered"

# ========================================================

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) ->str:
    try:
        edit_user = users_db[user_id-1]
        edit_user.username = username
        edit_user.age = age
        return f"user data updated"
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


# ========================================================

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) ->str:
    try:
        users_db.pop(user_id-1)
        return f"User id = {user_id} was deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')