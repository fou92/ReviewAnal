from services.similarity import analyze_need
from services.steam_api import get_reviews, get_game_title, browse_img_src
from dotenv import load_dotenv
import os

def similarity_analyze(url, need):
    try:
        reviews = get_reviews(url)
        if len(reviews) == 0:
            return {
                "score": 0
            }

        scores = analyze_need(need, reviews)
        descending_sorted = sorted(scores, reverse=True)
        top50 = descending_sorted[:50]

        mean = sum(top50)/len(top50)
        score = float(mean)
        return {
            "score": score, "title": get_game_title(url), "imgurl": browse_img_src(url)
        }
    except Exception as e:
        return {"error": f"{str(e)} in similarity_analyze"}