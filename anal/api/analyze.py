from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
from services.similarity import analyze_need
from services.steam_api import get_reviews

app = FastAPI()

def analyze(url, need):
    reviews = get_reviews(url)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    scores = analyze_need(need, reviews, model)

    descending_sorted = sorted(scores, key=scores.get, reverse=True)

    top50 = descending_sorted[:50]
    return {
        "score": float(top50.mean())
    }