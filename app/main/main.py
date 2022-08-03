from fastapi import FastAPI

from .routes import animals

app = FastAPI()

app.include_router(animals.router)
