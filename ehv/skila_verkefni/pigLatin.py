pyg = 'ay'
pyg_yay = 'yay'

while True:
    word = input("Enter a word: ")
    if word == '.':
        break
    else:   
        first = word[0]      
        if first in ('aeiou'): 
            new_word = word + pyg_yay
            print(new_word)
        elif len(word) >= 5:
            new_word = word[-4:] + word[0:3] + pyg
            print(new_word)
        elif len(word) == 3:
            new_word = word[1:3] + word[0] + pyg
            print(new_word) 