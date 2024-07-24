from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    account: str
    password: str