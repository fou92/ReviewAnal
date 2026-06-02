import json
import os

ROOT_PATH = os.getcwd().split("api")[0]
CACHE_PATH = os.path.join(ROOT_PATH,"data","cached_reviews.json")


def save_reviews(app_id, reviews):
    try:
        with open(CACHE_PATH, "r",encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data={}

    data[app_id] = reviews
    with open(CACHE_PATH, "w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

def load_reviews(app_id):
    try:
        with open(CACHE_PATH, "r",encoding="utf-8") as f:
            data = json.load(f)
        return data.get(app_id,[])
    except FileNotFoundError:
        return []