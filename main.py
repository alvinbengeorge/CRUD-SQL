from fastapi import FastAPI
from routes.add import router as add_router
from routes.get import router as get_router
from routes.delete import router as delete_router
from routes.update import router as update_router

app = FastAPI()
app.include_router(add_router)
app.include_router(get_router)
app.include_router(delete_router)
app.include_router(update_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}