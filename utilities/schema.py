from pydantic import BaseModel

class LogData(BaseModel):
    user: str
    description: str