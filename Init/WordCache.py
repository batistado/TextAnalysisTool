import os
import re

from bs4 import BeautifulSoup
from Init.BaseInit import BaseInit


class WordCache(BaseInit):
    def __init__(self):
        self._cache = dict()
        self._cache_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.path.abspath('Cache/Words/'))
        self.parse_cached_files()

    def parse_cached_files(self):
        for file in self.get_files(self._cache_path):
            type = re.search(r'-(\w+)\.txt$', file).group(1).strip()
            with open(file) as f:
                soup = BeautifulSoup(f, 'html.parser')
                table = soup.find('table', attrs={'class': "highlight tab-size js-file-line-container"})
                for row in table.find_all('td', attrs={'class': "blob-code blob-code-inner js-file-line"}):
                    self._cache[row.text.strip().lower()] = type

    def get_word_type(self, word):
        lower_word = word.lower()
        if lower_word in self._cache:
            return self._cache[lower_word]

        return None
