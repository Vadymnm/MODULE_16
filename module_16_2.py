from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/{user_id}")
async def user_id(user_id: int = Path(ge=1, le=100, description='Enter UserID',example='5')) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def name_age(username: str = Path(min_length=5, max_length=20, description= 'Enter username', example= 'UrbanUser')
                   , age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> dict:
    return {"message": f"Информация о пользователе: Имя: {username}, Возраст: {age}"}


