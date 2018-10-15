import string

vowels = set("a,e,i,o,u")
word = input("Enter a word: ")

while word != ".":
    first_word = word[0]
    if first_word in vowels:
        pig_word = word + "yay"
    elif len(word) < 3:
        pig_word = word + "yay"
    else:
        pig_word = word
        for index, letter in enumerate(word):
            if letter in vowels:
                consonants = word[:index]
                rest = word[index:]
                pig_word = rest + consonants
                break
        pig_word = pig_word + "ay"
    print(pig_word)
    word = input("Enter a word: ")



