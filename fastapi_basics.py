from fastapi import Depends,FastAPI,HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel


class user(BaseModel):
    name: str
    age: int
    adress: str
    
app =  FastAPI()

@app.get("/test/{item_id}")
async def test(item_id: int ,queary: bool =1):
    return {queary:item_id}
@app.post("/create/")
async def createUser(user: user):
    return {"user":user}