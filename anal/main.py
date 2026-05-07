from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from sentence_transformers import SentenceTransformer
from api.analyze import similarity_analyze
from dotenv import load_dotenv
from services.steam_api import get_reviews
import os

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://strev.fastapicloud.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = SentenceTransformer('./models/paraphrase-MiniLM-L3-v2')

templates = Jinja2Templates(directory = "templates")

class RequestData(BaseModel):
    url: str
    need: str

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", request={"request": request})

@app.post("/analyze")
async def analyze_api(data: RequestData):
    url = data.url
    need = data.need

    res = similarity_analyze(url, need, model)
    return res