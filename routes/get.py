from fastapi.routing import APIRouter as Router

from utilities.database import Database

router = Router()
db = Database()

@router.get("/get")
async def get_all():
    return db.show_all()
