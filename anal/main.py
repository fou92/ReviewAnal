from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from api.analyze import similarity_analyze as analyze, similarity_analyze
from services.steam_api import get_reviews

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://strev.fastapicloud.dev/"],  # 개발용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")

class RequestData(BaseModel):
    url: str
    need: str

templates = Jinja2Templates(directory = "templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", request={"request": request})

@app.post("/analyze")
async def analyze_api(data: RequestData):
    url = data.url
    need = data.need

    reviews = get_reviews(url)
    res = similarity_analyze(url, need)
    return res

