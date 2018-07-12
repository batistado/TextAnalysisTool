class Word:
    def __init__(self, name, category=None, meaning=None):
        self.name = name
        self.category = category
        self.meaning = meaning
        self.total_occurence = 1
        self.is_common = False

    def increment_total_occurrence(self):
        self.total_occurence += 1

    def change_to_common(self):
        self.is_common = True

    def print_word_info(self):
        print('Category: {}'.format(self.category))
        print('Total Occurences: {}'.format(self.total_occurence))
        print('Meaning: {}'.format(self.meaning))
        type = 'common' if self.is_common else 'exclusive'
        print('Word type: {}'.format(type))
