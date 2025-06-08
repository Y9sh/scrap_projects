import os
import json
from dataset.commonW import common_words

# Load slang dict
with open(os.path.join(os.path.dirname(__file__), 'dataset','slang.json'), 'r', encoding='utf-8') as f:
    slang_dict = json.load(f)

def replace_slang(tokens):
    replaced = []
    for tok in tokens:
        lowered = tok.lower()
        if lowered in slang_dict and lowered not in common_words:
            expanded = slang_dict[lowered].split()
            replaced.extend(expanded)
        else:
            replaced.append(tok)
    return replaced
