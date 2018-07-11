import requests
import os

from string import ascii_lowercase
from bs4 import BeautifulSoup
from Init.BaseInit import BaseInit


class MeaningCache(BaseInit):
    def __init__(self):
        self._meaning_cache = dict()
        self._cache_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.path.abspath('Cache/Meanings/'))
        if not os.path.exists(self._cache_path) and len(os.listdir(self._cache_path)) > 0:
            self.fetch_files()
        else:
            for file in self.get_files(self._cache_path):
                with open(file) as f:
                    self.cache_files(f)

    def fetch_files(self):
        os.mkdir(self._cache_path)

        for letter in ascii_lowercase:
            uri = 'http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_{}.html'.format(letter)
            r = requests.get(uri)
            with open(os.path.join(self._cache_path, '{}.txt'.format(letter)), 'w', encoding="utf-8") as f:
                f.write(r.text)
                self.cache_files(r.text)

    def cache_files(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        for para in soup.find_all('p'):
            word = self.get_element(para, 'b').lower()
            if word not in self._meaning_cache:
                self._meaning_cache[word] = '\t'.join([self.get_element(para, 'i'), para.text.strip()])
            else:
                self._meaning_cache[word] = '\n'.\
                    join([self._meaning_cache[word], self.get_element(para, 'i'), para.text.strip()])

    def get_meaning(self, word):
        lower_word = word.lower()
        if lower_word in self._meaning_cache:
            return self._meaning_cache[lower_word]

        return None
