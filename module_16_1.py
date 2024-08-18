from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/main")
async def welcome() -> dict:
    return {"message": "Main page"}


@app.get("/user/admin")
async def admin_() -> dict:
    return {"message": "Вы вошли как aдминистратор"}


@app.get("/user/{user_id}")
async def user_id(user_id: str) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{user_name}/{user_age}")
async def name_age(user_name: str, user_age: int) -> dict:
    return {"message": f"Информация о пользователе: Имя: {user_name}, Возраст: {user_age}"}


@app.get("/user")
async def name_age(user_name: str, user_age: int) -> dict:
    return {"message": f"Информация о пользователе: Имя: {user_name}, Возраст: {user_age}"}
