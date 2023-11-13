from fastapi import FastAPI
from routes.add import router as add_router
from routes.get import router as get_router

app = FastAPI()
app.include_router(add_router)
app.include_router(get_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}