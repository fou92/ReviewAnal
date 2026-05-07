from sentence_transformers import util


def analyze_need(user_need, reviews, model):
    user_emb = model.encode(user_need, batch_size=5)
    review_emb = model.encode(reviews, batch_size=5)

    scores = util.cos_sim(user_emb, review_emb)[0]

    return scores