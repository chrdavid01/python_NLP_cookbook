import nltk

import story

tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

sentences = tokenizer.tokenize(story.story)

print("hello")
