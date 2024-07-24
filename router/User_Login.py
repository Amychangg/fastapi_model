from fastapi import APIRouter, HTTPException
from schema.Auth_Schema import UserLogin

router = APIRouter(
    prefix = '/prefix')


@router.get("/items/")
def read_items() -> str:
    return '111'



@router.post("/login")
async def login(request: UserLogin):
    # 在這裡驗證用戶憑證
    user = db.verify_user(request.account, request.password)  # 假設你有一個 db 物件來處理數據庫
    if user:
        return {"username": user.username, "token": "your_jwt_token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")



@router.get("/user")
async def get_user(token: str):
    # 根據 token 獲取用戶信息
    user = db.get_user_by_token(token)  # 假設你有一個 db 物件來處理數據庫
    if user:
        return {"username": user.username}
    raise HTTPException(status_code=404, detail="User not found")
