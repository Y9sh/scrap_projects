import nltk
#rom nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer

#nltk.download("averaged_perceptron_tagger")

#nltk.download('wordnet')       # WordNet lexical database
nltk.download('omw-1.4')       # Optional: for multilingual support
#nltk.download('punkt')         # For tokenization (if needed)



#sentence = "I'm very happy asleep running training you"
#tokens = word_tokenize(sentence)
#print(tokens)

#stopwords = set(stopwords.words('english'))
#filtered_tokens = [word for word in tokens if word.lower() not in stopwords]
#print(filtered_tokens)


#lemmatizer = WordNetLemmatizer()
#lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
#print(lemmatized_tokens)


#tokens = ["I", "never", "liked", "you", "but", "you're", "cool"]
#print(nltk.pos_tag(tokens))


from nltk.corpus import wordnet as wn

# Get synsets (sets of synonyms) for a word
synsets = wn.synsets('car')
print(synsets)

# Get the first synset
car = synsets[0]
print("Definition:", car.definition())
print("Examples:", car.examples())
print("Synonyms:", car.lemma_names())

# Hypernym (more general term)
print("Hypernyms:", car.hypernyms())

# Hyponym (more specific terms)
print("Hyponyms:", car.hyponyms())