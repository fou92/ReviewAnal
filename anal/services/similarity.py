from sentence_transformers import util
from steam_api import get_reviews
# from json import

def analyze_need(user_need, reviews, model):
    user_emb = model.encode(user_need)
    review_emb = model.encode(reviews)

    scores = util.cos_sim(user_emb, review_emb)

    return scores