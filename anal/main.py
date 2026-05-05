from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sentence_transformers import SentenceTransformer

from api.analyze import analyze, RequestData
from services.steam_api import get_reviews

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", request={"request": request})

@app.post("/analyze")
async def analyze(data: RequestData):
    model = SentenceTransformer("")

    reviews = get_reviews(data.url)
    res = analyze(data.url, data.need)
    return templates.TemplateResponse(res)