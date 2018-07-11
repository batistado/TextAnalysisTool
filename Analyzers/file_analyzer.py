import os

from Analyzers.text_analyzer import TextAnalyzer


class FileAnalyzer(TextAnalyzer):
    def __init__(self, filename):
        if not os.path.exists(filename):
            self.file = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        else:
            self.file = filename

        with open(self.file, encoding="utf-8") as f:
            super().__init__(f.read())
