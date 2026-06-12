from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

# load_dotenv()
# HF_TOKEN = os.getenv("HF_TOKEN")
#
# client = InferenceClient(
#     provider="auto",
#     api_key=HF_TOKEN,
# )
model = "sentence-transformers/paraphrase-MiniLM-L3-v2"

# def get_embedding(text):
#     try:
#         response = requests.post(
#             API_URL,
#             headers=headers,
#             json={
#                 "inputs": text
#             },
#             timeout=30
#         )
#         print(response.status_code)
#
#         return np.array(response.json())
#     except Exception as e:
#         return {"error": str(e)}

def analyze_need(user_need, reviews):
    try:
        if len(reviews) == 0:
            print("no reviews or failed to load")
            raise Exception
        scores = client.sentence_similarity(sentence=user_need, other_sentences=reviews, model=model)
        return scores
    except Exception as e:
        raise e