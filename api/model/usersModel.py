from pydantic import BaseModel

class UsersModel(BaseModel):
    idUser : int
    name : str
    age : int

    class Config:
        orm_mode = True