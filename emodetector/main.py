from mainPipeline import main_pipeline

tests = [
"OMG I REALLY love you sooo much!!! 💖😭 #blessed @crush 35"
]

for text in tests:
    print(f"\nText: {text}")
    print("Final Tokens:", main_pipeline(text))