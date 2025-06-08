import regex

known_entities = {
    "emotion": {"love", "hate", "joy", "fear"},
    "relationship": {"mom", "dad", "bae", "crush"},
    "existential": {"life", "death", "god"},
    "social": {"you", "friend", "@someone"},
}

booster_words = {
    "very", "really", "so", "super", "extremely", "hella", "totally", "absolutely", "too", "such", "highly", "deeply"
}

known_entities_map = {}
for category, words in known_entities.items():
    for w in words:
        known_entities_map[w.lower()] = category.upper()


def detect_entities(tokens):
    result = []
    i = 0

    while i < len(tokens):
        tok = tokens[i]

        # Emphasis: All caps
        if tok.isalpha() and tok.isupper() and len(tok) > 1:
            result.append("EMPH_" + tok)
            i += 1
            continue

        # Booster words
        if tok.lower() in booster_words:
            result.append("BOOST_" + tok)
            i += 1
            continue

        # Mention
        if tok.startswith("@"):
            result.append("MENTION")
            i += 1
            continue

        # Repeated punctuation
        if regex.fullmatch(r'[!?]{2,}', tok):
            if result:
                prev = result.pop()
                result.append("EMPH_" + prev)
            result.append("EMPH_PUNCT")
            i += 1
            continue

        # Entities
        if tok.lower() in known_entities_map:
            tag = f"ENTITY_{known_entities_map[tok.lower()]}"
            result.append(f"{tag}_{tok}")
            i += 1
            continue

        # Default
        result.append(tok)
        i += 1

    return result



