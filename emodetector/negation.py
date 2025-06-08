from dataset.negationCues import negation_stop, negation_cues


def handle_negations(tokens,negation_stop =negation_stop, negations_cues =negation_cues):
    result =[]
    negating = False
    for tok in tokens:
        lowered = tok.lower()
        if lowered in negations_cues :
            negating = True
            result.append(lowered)
            continue
        if tok in negation_stop:
            negating = False
            result.append(tok)
            continue
        if negating:
            result.append("NEG_" + tok)
        else:
            result.append(tok)
    return result
