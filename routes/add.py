from fastapi.routing import APIRouter as Router
from utilities.database import Database
from utilities.schema import LogData

router = Router()

@router.post("/add")
async def append(data: LogData):
    db = Database()
    db.insert(data)
    return {"status": "success"}