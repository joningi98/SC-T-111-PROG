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
        print("Documents not found")
        exit()


def file_options(doc_list):
    print("What would you like to do?\n1. Search Documents\n2. Print Document\n3. Quit Program")
    choice = int(input(""))
    if choice == 1:
        search_documents(doc_list)
    if choice == 2:
        print_documents(doc_list)
    if choice == 3:
        quit_the_program()


def quit_the_program():
    print("Exiting program.")
    quit()


def search_documents(doc_list):
    search_word_dict = {}
    value_set = set([])
    try:
        search_word = input("Enter search words: ").lower()
        if ' ' in search_word:
            target1, target2 = search_word.split()
            search_key = target1, target2
        else:
            search_key = search_word
        for x, my_list in enumerate(doc_list, start=-1):
            if not my_list:
                continue
            for line in my_list:
                line = line.split()
                for word in line:
                    lower_word = word.lower().strip(string.punctuation)
                    if lower_word in search_key:
                        search_word_dict.setdefault(lower_word, []).append(x)
        for values in search_word_dict.values():
            value_set.update(values)
        if len(value_set) == 0:
            print("No match.")
        else:
            print("Documents that fit search:", *value_set)
            print('')
    except KeyError:
        print("No match.")


def print_documents(doc_list):
    try:
        doc = int(input("Enter document number: "))
        print("Document #{}".format(doc))
        for line in doc_list[doc + 1]:
            line.strip('\n')
            if line == ' ':
                continue
            elif line[0] == ' ':
                line.strip()
                print(line)
            else:
                print(line)
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
