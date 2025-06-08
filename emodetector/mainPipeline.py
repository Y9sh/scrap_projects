from tokenizer import BaeTokenizer
from slang import replace_slang
from emoji import replace_emojis
from entity_emphasis import detect_entities
from negation import handle_negations
from pos_guesser import guess_pos, lemmatize_tagged
from contraction import  expand_contractions
import html

def main_pipeline(text):

    # Step 1: Tokenize + Normalize
    tokens = BaeTokenizer(text)
    print("1. Tokens:", tokens)

    tokens = expand_contractions(tokens)
    print("Contraction:", tokens)

    # Step 2: Slang Replacement
    tokens = replace_slang(tokens)
    print("2. Slang Replaced:", tokens)

    tokens = replace_emojis(tokens)
    print("Emoji replace:", tokens)

    # Step 3: Apply Negation Scope
    tokens = handle_negations(tokens)
    print("3. Negation Scoped:", tokens)

    tokens = detect_entities(tokens)
    print("Detect entities:")

    # Step 4: POS Guessing
    tagged = guess_pos(tokens)
    print("4. POS Tagged:", tagged)

    # Step 5: Lemmatization
    lemmas = lemmatize_tagged(tagged)
    print("5. Lemmatized:", lemmas)


    def clean_token(tok):
        # Decode HTML entities, trim, and lowercase
        tok = html.unescape(tok)
        tok = tok.strip()
        return tok.lower()

    
    final_tokens = [clean_token(t) for t in tokens]
    print("Final Tokens:", final_tokens)
    return final_tokens



