import sys
print (f"Work with {sys.version}")
 
from fastapi import FastAPI
from app import main
app = FastAPI()
main.main(app)


from dal.repository.usersRepo import UsersRepo
from database.database import session
from database.users import Users

repo = UsersRepo(session, Users)


result= repo.getAll()
for row in result:
    print(f"{row.idUser} - {row.name} - {row.age} ")

print("end")

