def open_file(filename):
    with open(filename, 'r') as file:
        word_list = []
        for word in file.readlines():
            word_list.append(word.strip())
    return word_list


def find_word(word_list):
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def main():
    filename = input("Enter file: ")
    word_list = open_file(filename)
    longest_word = find_word(word_list)
    print("Longest word is '{}' of length {}".format(longest_word, len(longest_word)))


main()