from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from auth_fastapi.router import User_Login



app = FastAPI()

app.include_router(User_Login.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

@app.get("/")
def read_root():
    return {"Hello": "World"}







if __name__ == '__main__':
    uvicorn.run("main:app", host="192.168.68.59", port=7777, reload=True)