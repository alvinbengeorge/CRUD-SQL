from fastapi import APIRouter as Router
from utilities import Database, LogData

router = Router()
db = Database()

@router.delete("/delete/{id}")
async def delete(id: int):
    db.delete(id)
    return {"status": "success"}