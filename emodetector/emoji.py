import regex

emoji_sentiment = {
    "😊": "positive",   
    "😢": "negative",   
    "❤️": "positive",   
    "😭": "sad",        
    "😍": "flirty",     
    "🔥": "intense",    
    "💔": "heartbroken",
    "😘": "flirty",     
    "💪": "motivational",
    "😎": "cool",       
    "😡": "angry",      
    "😱": "scared", 
    "💖" : "shine" ,
}

def replace_emojis(tokens):
    result = []
    
    for tok in tokens:
        if tok in emoji_sentiment:
            result.append(f"EMOJI_{emoji_sentiment[tok]}_{tok}")
        else:
            result.append(tok)
    
    return result
