import requests

def get_reviews(app_id):

    url = f"https://store.steampowered.com/appreviews/{app_id}"

    params ={
        "json":1,
        "num_per_page": 100,
        "language": "korean"
    }

    r=requests.get(url,params=params).json()

    return [review["review"] for review in r["reviews"]]