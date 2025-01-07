# Named Entity Recognition (NER):
# Identifying named entities like people, organizations, and locations.

from nltk import tokenize, pos_tag, ne_chunk

text = "The US President lives in the White House"
words = tokenize.word_tokenize(text)
pos_tags = pos_tag(words)
tree = ne_chunk(pos_tags)

print(tree)