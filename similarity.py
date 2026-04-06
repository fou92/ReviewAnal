from sentence_transformers import SentenceTransformer, util

def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def text_similarity(text1, text2):
    model = load_model()
    embeddings = model.encode([text1, text2], convert_to_tensor=True)

    similarity = util.cos_sim(embeddings[0], embeddings[1])

    return float(similarity)
