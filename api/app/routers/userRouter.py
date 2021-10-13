from typing import List
from fastapi import APIRouter
from model.usersModel import UsersModel
from bll.services.usersService import UsersService
from database.database import session

route = APIRouter(
    prefix="/user",
    tags=["User Router"]
    )

usersService = UsersService(session)
    
@route.get("/helloWorld", response_model=List[UsersModel]) 
async def helloWorld():
    return usersService.getAllUser()


@route.get("/byebye")
async def byebye():
    return {"message": "ByeBye"}