from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from services.similarity import analyze_need
from services.steam_api import get_reviews

app = FastAPI()

def similarity_analyze(url, need):
    reviews = get_reviews(url)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    scores = analyze_need(need, reviews, model)

    descending_sorted = sorted(scores, reverse=True)

    top50 = descending_sorted[:50]

    mean = sum(top50)/len(top50)
    return {
        "score": float(mean)
    }
#