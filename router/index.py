from fastapi import APIRouter

router = APIRouter(
    prefix = '/prefix')




@router.get("/items/")
def read_items() -> str:
    return '111'