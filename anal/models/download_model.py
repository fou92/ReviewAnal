from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

model.save('paraphrase-MiniLM-L3-v2')