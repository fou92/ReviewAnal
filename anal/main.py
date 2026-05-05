from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from sentence_transformers import SentenceTransformer
from starlette.middleware.cors import CORSMiddleware

from api.analyze import similarity_analyze as analyze, similarity_analyze
from services.steam_api import get_reviews

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestData(BaseModel):
    url: str
    need: str

templates = Jinja2Templates(directory = "templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", request={"request": request})

@app.post("/analyze")
async def analyze(data: RequestData):
    url = data.url
    need = data.need

    reviews = get_reviews(url)
    res = similarity_analyze(url, need)
    return res

