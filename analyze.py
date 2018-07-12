import argparse
import os
import traceback
import sys
import multiprocessing as mp

from collections import defaultdict

from Analyzers.file_analyzer import FileAnalyzer, TextAnalyzer
from Init.BaseInit import BaseInit


class Analyzer(BaseInit):
    def get_essays(self):
        essay_files = list()
        for essay_file in self.get_files(os.path.abspath('Cache/Essays')):
            essay_files.append(essay_file)

        return essay_files

    def merge_stats(self):
        for obj in self.analyzed:
            stats_obj = obj.get_stats()
            temp = set()
            for word in stats_obj.keys():
                if word not in self.word_stats:
                    self.word_stats[word] = stats_obj[word]
                    temp.add(word)
                else:
                    self.word_stats[word].increment_total_occurrence()
                    if word not in temp:
                        self.word_stats[word].change_to_common()

    def process_files(self, files):
        pool = mp.Pool(processes=4)

        for file in files:
            self.analyzed.append(pool.apply(FileAnalyzer, args=(file,)))

    def categorize_stats(self):
        for word, word_obj in self.word_stats.items():
            if word_obj.category is None:
                self.categorized_stats['No category'].append(word_obj.name)
            else:
                self.categorized_stats[word_obj.category].append(word_obj.name)
            if word_obj.is_common:
                self.exclusive_categoryized_stats['common'].append(word_obj.name)
            else:
                self.exclusive_categoryized_stats['exclusive'].append(word_obj.name)

    def print_summary(self):
        print('====================Summary====================')
        print('======= Based on word category')
        self._print_stats(self.categorized_stats)
        print('======= Based on word exclusivity')
        self._print_stats(self.exclusive_categoryized_stats)

    @staticmethod
    def _print_stats(data_dict):
        for cat in data_dict.keys():
            print('Category: {}'.format(cat))
            print('Total Count: {}'.format(len(data_dict[cat])))
            print('Words: {}'.format(', '.join(data_dict[cat])))
            print()

    def __init__(self, sentence=None, essay=False, files=None):
        self.analyzed = list()
        self.word_stats = dict()
        self.categorized_stats = defaultdict(list)
        self.exclusive_categoryized_stats = defaultdict(list)

        if essay:
            essays = self.get_essays()
            print('Select one of the following essays to analyze:')
            for idx, essay_file in enumerate(essays):
                print('{}. {}'.format(idx + 1, os.path.basename(essay_file)))

            self.analyzed.append(FileAnalyzer(essays[int(input('Enter your choice: ')) - 1]))

        if sentence:
            self.analyzed.append(TextAnalyzer(sentence))

        if files:
            self.process_files(files)

        self.merge_stats()
        self.categorize_stats()

    def get_word_stats(self, word):
        word_lower = word.lower()

        if word_lower in self.word_stats:
            return self.word_stats[word_lower]

        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tool for analyzing text in a sentence or an essay')
    parser.add_argument('--sentence', '-s', action='store', help='Analyze a sentence')
    parser.add_argument('--essay', '-e', action='store_true', help='Analyze from pre-defined essays')
    parser.add_argument('--files', '-f', action='store', nargs='+', help='Analyze from a list of specified files')
    args = parser.parse_args()

    try:
        analyzer = Analyzer(args.sentence, args.essay, args.files)
        analyzer.print_summary()

        while True:
            word = input('Enter a word to info: ')
            word_stat = analyzer.get_word_stats(word)

            if word_stat:
                print('WORD STATISTICS:')
                print()
                word_stat.print_word_info()
            else:
                print('Sorry. Word "{}" could not be found'.format(word))

    except Exception as ex:
        traceback.print_exc()
        sys.exit('Error while loading app: {}'.format(ex))
