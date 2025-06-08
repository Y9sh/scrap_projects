import regex

# STEP 1: Elongation Normalizer
def normalize_elongated(word):
    return regex.sub(r'(.)\1{2,}', r'\1\1', word)

# STEP 2: Tokenization
def tokenize_text(text):
    emoji_pattern = r'\p{Emoji}'
    hashtag_pattern = r'#\w+\b'
    word_pattern = r"[a-zA-Zà-ÿÀ-ß']+"
    punct_pattern = r'[^\w\s]+'
    url_pattern = r'https?://[^\s]+'
    number_pattern = r'\d+(?:\.\d+)?'

    combined = f"{url_pattern}|{hashtag_pattern}|{emoji_pattern}|{number_pattern}|{word_pattern}|{punct_pattern}"
    return regex.findall(combined, text, regex.UNICODE)

# STEP 3: Normalization
def normalize_tokens(tokens, keep_original=True):
    url_pattern = r'https?://[^\s]+'
    number_pattern = r'\d+(?:\.\d+)?'
    elongated_pattern = r'\b\w*(\w)\1{2,}\w*\b'
    word_pattern = r"[a-zA-Zà-ÿÀ-ß']+"

    normalized = []
    for tok in tokens:
        if regex.match(url_pattern, tok):
            normalized.append("<URL>")
        elif regex.match(number_pattern, tok):
            normalized.append("<NUM>")
        elif regex.match(elongated_pattern, tok):
            if keep_original:
                normalized.append(tok.lower())
            else:
                normalized.append(normalize_elongated(tok.lower()))
        elif regex.match(word_pattern, tok):
            normalized.append(tok.lower())
        else:
            normalized.append(tok)
    return normalized

# STEP 4: Main pipeline
def BaeTokenizer(text, keep_original=True):
    raw_tokens = tokenize_text(text)
    return normalize_tokens(raw_tokens, keep_original=keep_original)

