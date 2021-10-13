from fastapi import APIRouter

route = APIRouter(
    prefix="/user",
    tags=["User Router"]) 
    
@route.get("/helloWorld") 
async def helloWorld():
    return {"message": "Hello World"}


@route.get("/byebye")
async def byebye():
    return {"message": "ByeBye"}