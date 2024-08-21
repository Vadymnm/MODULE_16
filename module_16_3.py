from fastapi import FastAPI, Path

app = FastAPI()

users = {'1':'Имя: Example, возраст: 18'}

@app.get("/user")
async def get_all() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str = Path(min_length=5, max_length=20, description= 'Enter username', example= 'UrbanUser')
                      , age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    current_index = str(int(max(users,key=int))+1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int = Path(ge=1, le=100, description='Enter user ID', example='4')
                      , username: str = Path(min_length=5, max_length=20, description= 'Enter username', example= 'UrbanUser')
                      , age: int= Path(ge=18, le=120, description='Enter age', example='24')) ->str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str = Path(description='Enter UserID',example='5')) ->str:
    users.pop(user_id)
    return f"User {user_id} was deleted"

