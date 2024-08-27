import nltk
# import spacy
# from nltk.stem.snowball import SnowballStemmer
# from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist

import story

text = story.story
if "\n" in text:
    text = text.replace("\n", " ")

words = ["duck", "geese", "cats", "books"]

nltk_words = nltk.tokenize.word_tokenize(text)

# tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
# stopwords = nltk.corpus.stopwords.words("english")
# freq_dist = FreqDist(word.lower() for word in nltk_words)
# frequent_words = [(word, freq_dist[word]) for word in freq_dist.keys()]
# sorted_words = sorted(frequent_words, key=lambda tup: tup[1])



# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)

# nltk_sentences = tokenizer.tokenize(story.story)
# spacy_sentences = [sentence.text for sentence in doc.sents]

# nltk_words = [word for word in nltk_words if word.lower() not in stopwords]
# spacy_words = [token.text for token in doc]

# spacy_pos = [token.pos_ for token in doc]
# spacy_words_pos = list(zip(spacy_words, spacy_pos))

# nltk_pos = nltk.pos_tag(nltk_words)

# stemmer = SnowballStemmer("english")
# stemmed_words = [stemmer.stem(word) for word in nltk_words]

# lemmatizer = WordNetLemmatizer()
# lemmatized_words = [lemmatizer.lemmatize(word) for word in words]


print("hello")
