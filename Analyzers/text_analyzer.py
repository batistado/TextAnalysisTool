import re

from collections import defaultdict

from Init.MeaningCache import MeaningCache
from Init.WordCache import WordCache
from Init.Word import Word


class TextAnalyzer:
    def __init__(self, data):
        self._data = data
        self._word_stats = dict()
        self._analyze_data()

    def _analyze_data(self):
        for word in self._data.split():
            word = re.search(r'(\w+)', word).group(1).strip().lower()
            word_type = WordCache().get_word_type(word)
            word_obj = Word(name=word, category=word_type, meaning=MeaningCache().get_meaning(word))
            if word not in self._word_stats:
                self._word_stats[word] = word_obj
            else:
                self._word_stats[word].increment_total_occurrence()

    def get_stats(self):
        return self._word_stats
