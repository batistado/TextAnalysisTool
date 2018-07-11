import argparse
import os
from pprint import pprint
import multiprocessing as mp

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
            for word in stats_obj.keys():
                if word not in self.full_stats:
                    self.full_stats[word] = stats_obj[word]
                else:
                    self.full_stats[word]['count'] += 1

    def process_files(self, files):
        pool = mp.Pool(processes=4)

        for file in files:
            self.analyzed.append(pool.apply(FileAnalyzer, args=(file,)))

    def __init__(self, sentence=None, essay=False, files=None):
        self.analyzed = list()
        self.full_stats = dict()
        self.threads = list()

        if sentence:
            self.analyzed.append(TextAnalyzer(sentence))

        if essay:
            essays = self.get_essays()
            print('Select one of the following essays to analyze:')
            for idx, essay_file in enumerate(essays):
                print('{}. {}'.format(idx + 1, os.path.basename(essay_file)))

            self.analyzed.append(FileAnalyzer(essays[int(input('Enter your choice: ')) - 1]))

        if files:
            self.process_files(files)

        self.merge_stats()
        pprint(self.full_stats)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tool for analyzing text in a sentence or an essay')
    parser.add_argument('--sentence', '-s', action='store', help='Analyze a sentence')
    parser.add_argument('--essay', '-e', action='store_true', help='Analyze from pre-defined essays')
    parser.add_argument('--files', '-f', action='store', nargs='+', help='Analyze from a list of specified files')
    args = parser.parse_args()
    Analyzer(args.sentence, args.essay, args.files)
