from fastapi import FastAPI

from app.main.routers import animals

app = FastAPI()

app.include_router(animals.router)
