import string


def open_file(filename):
    try:
        word_list = [[]]
        with open(filename, 'r') as data_file:
            data_file = data_file.readlines()
            counter = 0
            for line in data_file:
                if line == "<NEW DOCUMENT>\n":
                    word_list.append([])
                    counter += 1
                    continue
                line = line.split()
                for word in line:
                    word_list[counter].append(word)
        return word_list
    except FileNotFoundError:
        print("Documents not found")
        exit()


def file_options(word_list):
    print("1. Search Documents\n2. Print Document\n3. Quit Program")
    choice = int(input(""))
    if choice == 1:
        search_documents(word_list)
    if choice == 2:
        print_documents(word_list)
    if choice == 3:
        quit_the_program()


def quit_the_program():
    print("Exiting program.")
    quit()


def search_documents(word_list):
    search_word_dict = {}
    value_set = set([])
    try:
        search_word = input("Enter search words: ").lower()  # .join(str(x) for x in L)
        if ' ' in search_word:
            target1, target2 = search_word.split()
            search_key = target1, target2
        else:
            search_key = search_word
        for x, my_list in enumerate(word_list, start=-1):
            if not my_list:
                continue
            for word in my_list:
                lower_word = word.lower().strip(string.punctuation)
                if word in search_key:
                    search_word_dict.setdefault(lower_word, []).append(x)
        for values in search_word_dict.values():
            value_set.update(values)
        if len(value_set) == 0:
            print("No match.")
        else:
            print("Documents that fit search:", *value_set)
    except KeyError:
        print("No match.")


def print_documents(word_list):
    try:
        doc = int(input("Enter document number: "))
        print("Document #{}".format(doc))
        print(*word_list[doc + 1], end=' ')
    except IndexError:
        print("No such document")
        quit()


def main():
    filename = input("Document collection: ")
    data_read = True
    while data_read:
        data_file = open_file(filename)
        file_options(data_file)


main()
