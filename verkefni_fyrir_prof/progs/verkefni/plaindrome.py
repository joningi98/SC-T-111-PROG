class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word_backwards = word[::-1].lower()
        if word.lower() == word_backwards:
            return True

print(Palindrome.is_palindrome('Deleveled'))