import requests
from similarity import text_similarity

def get_reviews(normal_url, num_reviews=30):
    game_id = normal_url.split("/app/")[1].split("/")[0]
    url = f"https://store.steampowered.com/appreviews/{game_id}?json=1&num_per_page={num_reviews}"
    
    params = {
        "json": 1,
        "num_per_page": num_reviews,
        "language": "korean",
        "filter": "recent",
        "purchase_type": "all"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    reviews = []
        
    for review in data["reviews"]:
        reviews.append({
            "review": review["review"],
            "recommended": review["voted_up"],
            "playtime": review["author"]["playtime_forever"]
        })
    
    return reviews

def reviews_from_dict(reviews_dict):
    reviews = []
    for review in reviews_dict:
        reviews.append(review["review"])
    return reviews

def get_similar_reviews(text_input, reviews):
    similar_reviews = []
    for review in reviews:
        if text_similarity(text_input, review) >= 0.7:
            similar_reviews.append(review)
    return similar_reviews