from fastapi import APIRouter as Router, Request
from utilities import Database, LogData

router = Router()
db = Database()

@router.put("/update/{id}")
async def update(req: Request, id: int, data: LogData):
    db.update(id, data)
    return {"message": "Updated successfully!"}