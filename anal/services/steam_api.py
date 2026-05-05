import requests
from similarity import analyze_need
from sentence_transformers import SentenceTransformer

def get_reviews(url):

    app_id = url.split("app")[-1].split("/")[1]
    api_url = f"https://store.steampowered.com/appreviews/{app_id}"

    params ={
        "json":1,
        "num_per_page": 100,
        "language": "korean"
    }
    res=requests.get(api_url,params=params)
    data = res.json()

    return [review["review"] for review in data["reviews"]]

print(get_reviews("https://store.steampowered.com/app/2780980/LOCKDOWN_Protocol/"))
