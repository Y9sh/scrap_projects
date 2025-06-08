# Update the emotion lexicon with vector-style components: pos, neg, neu, emoscore, weight
import random
import json

# Define scoring logic for vector components
def generate_vector(emotion, flavor):
    # Defaults
    pos, neg, neu = 0.0, 0.0, 0.0
    emoscore = round(random.uniform(0.6, 1.0), 2)
    weight = emoscore

    # Logic for emotional valence and flavor
    if emotion in ["joy", "love", "baddie", "teasing"]:
        pos = round(random.uniform(0.6, 1.0), 2)
    if emotion in ["sadness"]:
        neg = round(random.uniform(0.6, 1.0), 2)
    if emotion in ["lust", "horny", "lewd"]:
        pos = round(random.uniform(0.5, 0.8), 2)
        neg = round(random.uniform(0.1, 0.3), 2)
    if emotion in ["surprise"]:
        neu = round(random.uniform(0.3, 0.6), 2)

    # Normalize to ensure one emotional dominant vector
    total = pos + neg + neu
    if total == 0:
        neu = 1.0
    else:
        pos = round(pos / total, 2)
        neg = round(neg / total, 2)
        neu = round(neu / total, 2)

    return pos, neg, neu, emoscore, weight

# Rebuild lexicon with vectors
vector_jsonl = []
for emotion, props in emotions_rich.items():
    for word in props["words"]:
        pos, neg, neu, emoscore, weight = generate_vector(emotion, props["flavor"])
        vector_jsonl.append({
            "word": word,
            "emotion": emotion,
            "pos": pos,
            "neg": neg,
            "neu": neu,
            "emoscore": emoscore,
            "weight": weight,
            "valence": props["valence"],
            "flavor": props["flavor"],
            "contextual_neg": props["contextual_neg"],
            "category": props["category"]
        })

# Save the updated dataset
vector_jsonl_path = "/mnt/data/emotion_lexicon_vectorized.jsonl"
with open(vector_jsonl_path, "w") as f:
    for entry in vector_jsonl:
        f.write(json.dumps(entry) + "\n")

vector_jsonl_path
