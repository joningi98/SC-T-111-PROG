pyg = 'ay'
pyg_yay = 'yay'
vowels = set("aeiou")
while True:
    word = input("Enter a word: ")
    if word == '.':
        break
    elif word[0] in vowels:
            new_word = word + pyg_yay
            print(new_word)
    elif vowels & set(word):
        while word[0] not in vowels:
            word = word[1:] + word[0]
        print(word + 'ay')
    else:
        print(word + 'ay')
