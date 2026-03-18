import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load dataset
with open("data.json") as f:
    items = json.load(f)

contexts = [item["context"] for item in items]
context_embeddings = model.encode(contexts)

def get_prediction(user_input):

    user_embedding = model.encode([user_input])
    scores = cosine_similarity(user_embedding, context_embeddings)[0]

    top_index = scores.argmax()
    confidence = scores[top_index]

    result = items[top_index]

    text = user_input.lower()

    # SMART LOGIC
    if any(word in text for word in ["railway", "train", "platform"]):
        help_text = "Railway Help Desk"
        help_type = "railway"

    elif any(word in text for word in ["market", "crowd", "festival", "rush"]):
        help_text = "Security / Exit Points"
        help_type = "crowd"

    elif any(word in text for word in ["night", "alone", "street", "dark"]):
        help_text = "Police Station"
        help_type = "police"

    elif any(word in text for word in ["accident", "injury", "hospital"]):
        help_text = "Nearby Hospital"
        help_type = "medical"

    else:
        help_text = "Nearby Help Center"
        help_type = "general"

    # override
    result["help"] = help_text
    result["help_type"] = help_type

    # 🔥 ADD HERE
    result["confidence"] = round(float(confidence), 2)

    return result