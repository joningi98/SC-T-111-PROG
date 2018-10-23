class Sentence(object):
    def __init__(self, string=""):
        self.sentence_string = string

    def get_first_word(self):
        word = self.sentence_string.split()
        return word[0]

    def get_all_words(self):
        return self.sentence_string.split()

    def replace(self, index, new_word):
        word = self.sentence_string.split()
        if 0 <= index < len(word):
            word[index] = new_word
            self.sentence_string = " ".join(word)
            return self.sentence_string


