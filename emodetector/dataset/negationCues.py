negation_cues = {
    # Standard negations
    "not", "no", "never", "none", "nothing", "nobody", "nowhere", "neither", "nor",
    # Contractions
    "isn't", "aren't", "wasn't", "weren't", "don't", "doesn't", "didn't", "can't", 
    "couldn't", "won't", "wouldn't", "shouldn't", "hasn't", "haven't", "hadn't", "ain't",
    # Implicit/weak negations
    "hardly", "barely", "scarcely", "rarely", "seldom", "little", "few", 
    # Prefix-based
    "non", "un", "dis", "in", "im", "il", "ir", "a", "anti", "de", "counter", "mal",
    # Other constructs
    "without", "lacks", "lack", "missing", "absent", "deny", "denies", "denied", 
    "refuse", "refuses", "refused", "reject", "rejects", "rejected", "fail", "fails", 
    "failed", "avoid", "avoids", "avoided", "free", "minus", "opposite", "opposed",
    "opposing", "against", "stop", "stops", "stopped", "prevent", "prevents", "prevented"
}
negation_stop = {
    # Punctuation
    ".", "!", "?", ",", ";", ":", "(", ")", "[", "]", "{", "}", 
    # Conjunctions/contrast markers
    "but", "however", "although", "though", "yet", "still", "nevertheless", 
    "nonetheless", "instead", "except", "even", "despite", "unless", "rather", 
    "on the other hand", "conversely", "whereas", "while", "alternatively",
    # Clause boundaries
    "and", "or", "so", "therefore", "thus", "hence", "as a result", "consequently",
    # Discourse markers
    "in fact", "actually", "indeed", "furthermore", "moreover", "additionally"
}