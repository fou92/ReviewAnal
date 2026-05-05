import requests
from similarity import analyze_need
from sentence_transformers import SentenceTransformer

def get_reviews(url):

    app_id = url.split("/")[-1]

    params ={
        "json":1,
        "num_per_page": 100,
        "language": "korean"
    }
    r=requests.get(url,params=params).json()

    return [review["review"] for review in r["reviews"]]
