two_words = input("Input two words")

two_words.split()

two_words_list = two_words.split()
two_words_list

word1, word2 = two_words.split()  # Or spilt induvidualy with word.spilt

print(word1)
print(word2)

# Sort words 

word1_sorted = sorted(word1)
word2_sorted = sorted(word2)

print(word1_sorted)
print(word2_sorted)

# Check if words are anagrams

if word1_sorted == word2_sorted:
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")


####### Same thing but just with a function  ###############

def are_anagrams(word1, word2):
    """ Return True, if words are anagrams"""
    # 2. Sort the characters in the words
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    # 3. Check if words are identical.
    if word1_sorted == word2_sorted:
        return True
    else:
        return False


print("Anagram Test")

if are_anagrams(word1, word2):  # function returned True or False
    print("The words {} and {} are anagrams.".format(word1, word2))
else:
    print("The words {} and {} are not anagrams.".format(word1, word2))

##################### USING TRY EXCEPT #############################3

valid_input_bool = False

while not valid_input_bool:
    try:
        two_words = input("Enter two space separated words: ")
        word1, word2 = two_words.split()  # split the input string into a list of words
        valid_input_bool = True
    except ValueError:
        print("Bad Input")

if are_anagrams(word1, word2):  # function returned True or False
    print("The words {} and {} are anagrams.".format(word1, word2))
else:
    print("The words {} and {} are not anagrams.".format(word1, word2))
