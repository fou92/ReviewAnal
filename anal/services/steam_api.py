import requests

def get_reviews(url, num_per_page=100):

    app_id = url.split("app")[-1].split("/")[1]
    api_url = f"https://store.steampowered.com/appreviews/{app_id}"

    params ={
        "json":1,
        "num_per_page": num_per_page,
        "language": "korean",
        "filter": "recent",
        "purchase_type": "all"
    }
    res=requests.get(api_url,params=params)
    data = res.json()

    return [review["review"] for review in data["reviews"]]
