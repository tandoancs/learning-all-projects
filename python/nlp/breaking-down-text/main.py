import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "This is a sample sentence for tokenization. We are one."
words = word_tokenize(text)
sentences = sent_tokenize(text)

print(words)
print(sentences)
