import string

sentence = input("Input a sentence: ")

# Here you should add the missing part

unique_letters = []

for word in sentence:
    word = word.strip().replace(' ','')
    word = word.replace(',','').replace('.','').replace("'",'').replace('"','').replace("-",'').replace("?",'')
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)



print("Unique letters:", unique_letters)