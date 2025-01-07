
# Assigning grammatical tags to words (e.g., noun, verb, adjective).

from nltk import pos_tag, tokenize

text = "The quick brown fox jumps over the lazy dog"
words = tokenize.word_tokenize(text)
pos_tags = pos_tag(words)

print(pos_tags)