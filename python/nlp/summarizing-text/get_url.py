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


def read_text_from_url(url):
    """Reads the contents of a .txt file from a URL and returns them as a string.

    Args:
        url (str): The URL of the .txt file.

    Returns:
        str: The contents of the file as a string.

    Raises:
        requests.exceptions.RequestException: If there's an error making the HTTP request.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from URL: {e}")

# Get the current working directory
current_directory = os.getcwd()

# Specify the URL of the .txt file
url = "https://dantri.com.vn/kinh-doanh/quang-cao-ram-ro-temu-van-chua-dang-ky-hoat-dong-o-viet-nam-20241024094644845.htm"  # Replace with the actual URL

# Read the file contents from the URL
try:
    text_data = read_text_from_url(url)
    print(text_data)
except Exception as e:
    print(f"An error occurred: {e}")


# # Read text from a .txt file
# with open("source.txt", "r") as f:
#     vietnamese_text = f.read()


summarizer = VietnameseFrequencySummarizer()
summary = summarizer.summarize(vietnamese_text, 2)  # Get 2 sentences as summary

for sentence in summary:
    print(sentence)
