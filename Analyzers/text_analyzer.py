import re

from Init.MeaningCache import MeaningCache
from Init.WordCache import WordCache


class TextAnalyzer:
    def __init__(self, data):
        self._data = data
        self._word_stats = dict()

    def _analyze_data(self):
        for word in self._data.split():
            word = re.search(r'(\w+)', word).group(1).strip().lower()
            if word not in self._word_stats:
                self._word_stats[word] = {
                    'count': 1,
                    'category': WordCache().get_word_type(word),
                    'meaning': MeaningCache().get_meaning(word)
                }
            else:
                self._word_stats[word]['count'] += 1

    def get_stats(self):
        self._analyze_data()
        return self._word_stats