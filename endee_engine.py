import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_endee(query):
    try:
        with open("data.json") as f:
            data = json.load(f)

        contexts = [item["context"] for item in data]

        context_embeddings = model.encode(contexts)
        query_embedding = model.encode([query])

        scores = cosine_similarity(query_embedding, context_embeddings)[0]

        best_index = np.argmax(scores)
        best_score = scores[best_index]

        result = data[best_index]
        result["confidence"] = round(float(best_score), 2)

        return result

    except Exception as e:
        print("Safety Error:", e)
        return None


def search_product(query):
    try:
        with open("products.json") as f:
            products = json.load(f)

        results = []
        query_words = query.lower().split()

        for item in products:
            name = item["name"].lower()

            if any(word in name for word in query_words):
                results.append(item)

        if not results:
            results = products[:3]

        return results

    except Exception as e:
        print("Product Error:", e)
        return []