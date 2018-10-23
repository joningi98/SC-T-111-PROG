class Sentence(object):
    def __init__(self, sentence=''):
        self.sentence = sentence

    def get_first_word(self):
        return self.sentence.split()[0]

    def get_all_words(self):
        return self.sentence

    def replace(self, index, new_word):
        sentence_list = self.sentence.split()
        if 0 <= index < len(sentence_list):
            sentence_list[index] = new_word
            sentence_srt = " ".join(sentence_list)
            return sentence_srt
        else:
            print(None)


g1 = Sentence("I'm going home")

print(g1.get_first_word())
print(g1.get_all_words())
print(g1.replace(1, 'home'))
