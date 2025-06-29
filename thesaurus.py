from nltk.corpus import wordnet
from itertools import chain
import re

def longest_word(word_):
    synonyms = wordnet.synsets(word_)
    lemmas = [lemma.replace('_', ' ') for lemma in list(set(chain.from_iterable([word.lemma_names() for word in synonyms])))]
    lemmas.sort(key=lambda x: len(x))
    return lemmas[-1] if lemmas else word_



test = "your sentence goes here"

print(' '.join(longest_word(word) for word in test.split()))

