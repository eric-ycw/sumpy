import re


class Word:

    def __init__(self, base_str):
        self.base_str = base_str
        self.stripped_str = self.strip_word(base_str)
        self.weight = 1

    @staticmethod
    def strip_word(base_str):
        r_str = base_str.casefold()
        return re.sub('[^a-zA-Z]+', '', r_str)
