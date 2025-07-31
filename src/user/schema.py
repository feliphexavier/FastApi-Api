from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    name : str
    username : str
    email : EmailStr
    password : str

class UserResponseSchema(BaseModel):
    name: str
    username: str
    email: EmailStr