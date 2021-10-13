from app.routers import userRouter
def main(app):
    app.include_router(userRouter.route)
