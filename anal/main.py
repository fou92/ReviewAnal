from traceback import print_exc

from fastapi import FastAPI, Request
from fsspec.implementations import data
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from api.analyze import similarity_analyze
from dotenv import load_dotenv
from api.cache import load_reviews
from api.openai_api import response_gpt
from services.steam_api import url_to_id, get_reviews
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://strev.fastapicloud.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory = "templates")

class Preferences(BaseModel):
    story: int
    difficulty: int
    action: int
    strategy: int
    free: int
    calm: int

class RequestData(BaseModel):
    url: str
    need: str
    preferences: Preferences

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", request={"request": request})

@app.post("/analyze")
async def analyze_api(data: RequestData):
    try:
        url = data.url
        need = data.need
        prefs = data.preferences.model_dump()
        res = similarity_analyze(url, need, prefs)

        return res
    except Exception as e:
        return {"error": str(e)}

@app.post("/gpt")
async def gpt(data: RequestData):
    try:
        if bool(data.need):
            need = data.need
        else:
            need = "특이사항 없음"
        revs = get_reviews(data.url) # 와 시발 난 병신이야
        prefs = data.preferences.model_dump()

        res = response_gpt(need, prefs, revs)
        return res
    except Exception as e:
        print_exc()
        return {"error": str(e)}

