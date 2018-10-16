import string


def open_file(filename):
    word_list = []
    with open(filename, 'r') as data_file:
        data_file = data_file.readlines()
        for line in data_file:
            line = line.split()
            for word in line:
                stripped = word.strip(string.punctuation).lower()
                word_list.append(stripped)
    return word_list


def merge_words(word_list):
    merge_list = []
    for x in range(len(word_list)):
        if x + 1 == len(word_list):
            break
        else:
            the_words = word_list[x] + ',' + word_list[x+1]
            merge_list.append(the_words)
    return merge_list


def count_merged_word(merge_list):
    my_dict = {}
    for words in merge_list:
        words = words.split(',')
        words_tuple = tuple(words)
        if words_tuple in my_dict.keys():
            my_dict[words_tuple] += 1
        else:
            my_dict[words_tuple] = 1
    new_list = [(k, v) for k, v in my_dict.items()]
    print(new_list)


def main():
    file_name = input("Enter name of file: ")
    word_list = open_file(file_name)
    merge_list = merge_words(word_list)
    count_merged_word(merge_list)


main()
