from fastapi import FastAPI
from api.analyze import router

app = FastAPI()

app.include_router(router)