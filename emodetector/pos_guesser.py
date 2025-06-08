from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from dataset.pronouns import  english_pronouns
from dataset.verb import verb_dict
from dataset.adjectives import adjectives
from dataset.nouns import nouns

lemmatizer = WordNetLemmatizer()


def pos_to_wordnet(tag):
    if tag.startswith('VB'):
        return wordnet.VERB
    elif tag.startswith('NN'):
        return wordnet.NOUN
    elif tag.startswith('JJ'):
        return wordnet.ADJ
    elif tag.startswith('RB'):
        return wordnet.ADV
    else:
        return None

pronoun_map = {}
for categor, words in english_pronouns.items():
    for w in words:
        pronoun_map[w.lower()] = categor.upper()

verb_map ={}
for categor, words in verb_dict.items():
    for w in words:
        verb_map[w.lower()] = categor.upper()

adjectives_map ={}
for categor, words in adjectives.items():
    for w in words:
        adjectives_map[w.lower()] = categor.upper()    

nouns_map = {}
for categor, words in nouns.items():
    for w in words:
        nouns_map[w.lower()] = categor.upper()

def guess_pos(tokens):
    result = []

    for tok in tokens:
        lower = tok.lower()

        if lower in pronoun_map:
            tag = f"PRON_{pronoun_map[lower]}"
            result.append(f"{tag}_{tok}")
        elif lower in verb_map:
            tag = f"VERB_{verb_map[lower]}"
            result.append(f"{tag}_{tok}")
        elif lower in adjectives_map:
            tag = f"ADJ_{adjectives_map[lower]}"
            result.append(f"{tag}_{tok}")
        elif lower in nouns_map:
            tag = f"NOUN_{nouns_map[lower]}"
            result.append(f"{tag}_{tok}")
        elif tok[0].isupper():
            result.append("PROPN_" + tok)
        else:
            lemma = lemmatizer.lemmatize(lower)
            synsets = wordnet.synsets(lemma)

            if synsets:
                wn_pos = synsets[0].pos()
                tag = {
                    'n': "NOUN_GEN",
                    'v': "VERB_GEN",
                    'a': "ADJ_GEN",
                    's': "ADJ_GEN",  # satellite adjectives
                    'r': "ADV_GEN"
                }.get(wn_pos, "UNK")
            else:
                tag = "UNK"

        result.append(f"{tag}_{tok}")

    return result

def lemmatize_tagged(tagged_tokens):
    lemmas = []
    for tagged in tagged_tokens:
        tag, _, word = tagged.partition('_')
        lower = word.lower()

        pos = 'n'  # Default to noun
        if "VERB" in tag:
            pos = 'v'
        elif "NOUN" in tag:
            pos = 'n'
        elif "ADJ" in tag:
            pos = 'a'
        elif "ADV" in tag:
            pos = 'r'

        lemma = lemmatizer.lemmatize(lower, pos)
        lemmas.append(lemma)

    return lemmas


