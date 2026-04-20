from sentence_transformers import SentenceTransformer, util
from steam_api import get_reviews

model = SentenceTransformer('all-MiniLM-L6-v2')

def analyze_need(user_need, app_id):
    reviews = get_reviews(app_id)

    user_emb = model.encode(user_need, convert_to_tensor=True)
    review_emb = model.encode(reviews, convert_to_tensor=True)

    scores = util.cos_sim(user_emb, review_emb)[0]

    return float(scores.mean())