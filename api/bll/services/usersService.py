from model.usersModel import UsersModel
from dal.repository.usersRepo import UsersRepo
from database.users import Users

class UsersService:
    def __init__(self, session):
        self.repo = UsersRepo(session, Users)

    def getAllUser(self):
        result= self.repo.getAll()
        return result



    
