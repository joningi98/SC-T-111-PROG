import string


def open_file(filename):
    try:
        doc_list = [[]]
        with open(filename, 'r') as data_file:
            data_file = data_file.readlines()
            counter = 0
            for line in data_file:
                if line == "<NEW DOCUMENT>\n":
                    doc_list.append([])
                    counter += 1
                    continue
                line.strip()
                doc_list[counter].append(line)
        return doc_list
    except FileNotFoundError:
        print("Documents not found.")
        exit()


def file_options(doc_list):
    print("What would you like to do?\n1. Search Documents\n2. Print Document\n3. Quit Program")
    choice = int(input(""))
    if choice == 1:
        search_key = get_search_word()
        search_word_dict = search_documents(doc_list, search_key)
        print_search_word(search_word_dict, search_key)
    if choice == 2:
        print_documents(doc_list)
    if choice == 3:
        quit_the_program()


def quit_the_program():
    print("> Exiting program.")
    quit()


def get_search_word():
    search_word = input("> Enter search words: ").lower().split()
    return search_word


def search_documents(doc_list, search_key):
    search_word_dict = {}
    for x, my_list in enumerate(doc_list, start=-1):
        if not my_list:
            continue
        for line in my_list:
            line = line.split()
            for word in line:
                lower_word = word.lower().strip(string.punctuation)
                if lower_word in search_key:
                    search_word_dict.setdefault(lower_word, []).append(x)
    return search_word_dict


def print_search_word(search_word_dict, search_key):
    value_list = []
    for _ in search_key:
        value_list.append(set())
    for x, values in enumerate(search_word_dict.values()):
        value_list[x].update(values)
    k = set()
    for r in value_list:
        k = k.union(r)
    for r in value_list:
        k = k.intersection(r)
    if len(k) == 0:
        print("No match.")
    else:
        print("Documents that fit search:", *k)
        print('')


def print_documents(doc_list):
    try:
        doc = int(input("> Enter document number: "))
        print("Document #{}".format(doc))
        for line in doc_list[doc + 1]:
            stripped = line.rstrip()
            print(stripped)
        print('')
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
