# Gettysburg address analysis
# # count words , unique words
# Missing file use PyCharm

def make_word_list(a_file):
    word_list = []

    for line_str in a_file:          # Read a file line by line
        line_list = line_str.split()  # Split each line to a list of words
        for word in line_list:
            word = word.lower()
            word = word.strip(',.')
            if word != "--":
                word_list.append(word)  # Add words to a list of speech words
    return word_list

def make_unique(word_list):
    unique_list = []

    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
    return unique_list

gba_file = open("gettysburg.txt", "r")
speech_list = make_word_list(gba_file)
print("Speech Length: ", len(speech_list))
unique_list = make_unique(speech_list)
# p rint the sp e e ch and i t s l e n gths
print(unique_list)
print("Unique Length: ", len(make_unique(unique_list)))