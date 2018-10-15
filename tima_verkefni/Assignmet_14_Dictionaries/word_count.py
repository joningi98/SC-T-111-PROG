import string


def get_word_list(fpointer):
    word_list = []
    for line in fpointer:
        word_list.extend(line.strip().split())
    return word_list


def word_list_to_counts(word_list):
    word_count_dict = {}
    for word in word_list:
        lower_word = word.lower().strip(string.punctuation)
        if lower_word in word_count_dict:
            word_count_dict[lower_word] += 1
        else:
            word_count_dict[lower_word] = 1
    return word_count_dict


def dict_to_tuple(word_count_dict):
    word_count_tuples = []
    for key, val in word_count_dict.items():
        word_count_tuples.append((key, val))
    return word_count_tuples


def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer)
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list)
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))


main()
