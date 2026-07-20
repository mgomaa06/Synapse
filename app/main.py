from fastapi import FastAPI

from app.routers.inference import router as inference_router

app = FastAPI()

app.include_router(inference_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

