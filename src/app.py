from fastapi import FastAPI
from user.schema import UserSchema, UserResponseSchema, UserDB

from http import HTTPStatus
app = FastAPI()

DataBase = []

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/user", status_code=HTTPStatus.CREATED, response_model=UserDB)
async def create_user(user: UserSchema):
    user_db = UserDB(id=len(DataBase) + 1, **user.dict())
    DataBase.append(user_db)
    return user_db
@app.get("/user")
async def get_users():
    return DataBase