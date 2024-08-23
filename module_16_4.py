from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users_db = []
class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
async def get_all_users() -> List[User]:
    return users_db

# ===================================================================================
@app.post("/user/{username}/{age}")
async def create_message(user: User) -> str:
    user.id = len(users_db)
    if user.id == 0:
        user.id = 1
    else:
        user.id = user.id + 1
    print(user)
    return f"Message {user.id} is registered"

# ===================================================================================
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) ->str:
    try:
        edit_user = users_db[user_id-1]
        edit_user.username = username
        edit_user.age = age
        return f"user data updated"
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

# ===================================================================================
@app.delete("/user/{user_id}")
async def delete_user(user_id: int) ->str:
    try:
        users_db.pop(user_id-1)
        return f"User id = {user_id} was deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

