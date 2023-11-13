from fastapi.routing import APIRouter as Router

from utilities.database import Database

router = Router()

@router.get("/get")
async def get_all():
    db = Database()
    return db.show_all()
