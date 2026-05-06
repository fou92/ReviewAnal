from services.similarity import analyze_need
from services.steam_api import get_reviews

def similarity_analyze(url, need, model):
    reviews = get_reviews(url)
    scores = analyze_need(need, reviews, model)

    scores_list = scores.tolist()

    descending_sorted = sorted(scores_list, reverse=True)
    top50 = descending_sorted[:50]

    mean = sum(top50)/len(top50)
    score = float(mean)
    return {
        "score": score
    }