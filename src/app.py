from fastapi import FastAPI
from user.schema import UserSchema, UserResponseSchema
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/user")
async def create_user(user: UserSchema):
    user = user.dict()
    return UserResponseSchema(**user)