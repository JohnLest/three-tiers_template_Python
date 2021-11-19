from typing import List
from fastapi import APIRouter, HTTPException
from model.usersModel import UsersModel
from bll.services.usersService import UsersService
from database.database import session

route = APIRouter(
    prefix="/user",
    tags=["User Router"]
    )

usersService = UsersService(session)


@route.get("/helloWorld", response_model=List[UsersModel], status_code=200)
async def hello_world():
    return usersService.get_all_user()


@route.get("/make_coffee", status_code=201)
async def make_coffee():
    raise HTTPException(status_code=418, detail="I'm a teapot")
    return "Cup of coffee"


@route.get("/byebye")
async def byebye():
    return {"message": "ByeBye"}