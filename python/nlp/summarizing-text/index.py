import os
from collections import defaultdict
from heapq import nlargest
from string import punctuation

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# # Download required resources for Vietnamese
# nltk.download("punkt")
# nltk.download("stopwords")

# Use Vietnamese stopwords
stop_words = set(stopwords.words("english"))


class VietnameseFrequencySummarizer:
    def __init__(self, min_cut=0.1, max_cut=0.9):

        self._min_cut = min_cut
        self._max_cut = max_cut
        self._stopwords = stop_words.union(set(punctuation))

    def _compute_frequencies(self, word_sent):

        freq = defaultdict(int)
        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1
        # Frequencies normalization and filtering
        m = float(max(freq.values()))
        for w in list(freq.keys()):  # Iterate over a copy to allow deletion
            freq[w] = freq[w] / m
            if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
                del freq[w]
        return freq

    def summarize(self, text, n):
        """
        Return a list of n sentences
        which represent the summary of text.
        """
        sents = sent_tokenize(text)
        assert n <= len(sents)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        self._freq = self._compute_frequencies(word_sent)
        ranking = defaultdict(int)
        for i, sent in enumerate(word_sent):
            for w in sent:
                if w in self._freq:
                    ranking[i] += self._freq[w]
        sents_idx = self._rank(ranking, n)
        return [sents[j] for j in sents_idx]

    def _rank(self, ranking, n):
        """Return the first n sentences with the highest ranking"""
        return nlargest(n, ranking, key=ranking.get)


def read_text_file(file_path):
    """Reads the contents of a .txt file and returns them as a string.

    Args:
        file_path (str): The path to the .txt file.

    Returns:
        str: The contents of the file as a string.

    Raises:
        FileNotFoundError: If the file cannot be found.
        PermissionError: If the file cannot be read due to permission issues.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
            return text_content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")


# Get the current working directory
current_directory = os.getcwd()

# Specify the file path relative to the current directory
file_name = "source.txt"  # Replace with the actual file name
file_path = os.path.join(current_directory, file_name)

# Read the file contents
try:
    vietnamese_text = read_text_file(file_path)

except Exception as e:
    print(f"An error occurred: {e}")


# # Read text from a .txt file
# with open("source.txt", "r") as f:
#     vietnamese_text = f.read()


summarizer = VietnameseFrequencySummarizer()
summary = summarizer.summarize(vietnamese_text, 2)  # Get 2 sentences as summary

for sentence in summary:
    print(sentence)
