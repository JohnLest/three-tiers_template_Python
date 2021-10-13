from app.routers.userRouter import route

def main(app):
    app.include_router(route)
