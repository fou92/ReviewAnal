import requests
from similarity import analyze_need
from sentence_transformers import SentenceTransformer

def get_reviews(app_id):

    url = f"https://store.steampowered.com/appreviews/{app_id}"

    params ={
        "json":1,
        "num_per_page": 100,
        "language": "korean"
    }
    r=requests.get(url,params=params).json()

    return [review["review"] for review in r["reviews"]]

def to_sim(need, reviews, model="jhgan/ko-sroberta-multitask"):
    model = SentenceTransformer(model)
    sims = analyze_need(need, reviews, model)
    sims.sort(key=lambda x: x["score"], reverse=True)
    return sims