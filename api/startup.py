import sys
print (f"Work with {sys.version}")
 
from fastapi import FastAPI
from app import main
app = FastAPI()
main.main(app)
