from fastapi.routing import APIRouter as Router

from utilities.database import Database

router = Router()
db = Database()

@router.get("/get")
async def get_all():
    return db.show_all()

@router.get("/get/{id}")
async def get_by_id(id: int):
    return db.show_by_id(id)    

@router.get("/get/first/{num}")
async def get_first(num: int):
    return db.show_first(num)