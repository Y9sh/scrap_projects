import os 
import json

with open(os.path.join(os.path.dirname(__file__), 'dataset','contraction.json'), 'r', encoding='utf-8') as f:
    contractions = json.load(f)

def expand_contractions(tokens):
    expanded= []
    
    for tok in tokens:
        lower = tok.lower()
        if lower in contractions:
            expanded.extend(contractions[lower].split())
        else:
            expanded.append(tok)
    return expanded 

