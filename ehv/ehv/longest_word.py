longest_word = ''

with open('words.txt', 'r') as f:
    for word in f:
        stripped = word.strip().replace(' ','')
        if len(stripped) > len(longest_word):
            longest_word = stripped

length_of_longest_word = len(longest_word)

print("Longest word is '" + longest_word + "' of length", length_of_longest_word)
