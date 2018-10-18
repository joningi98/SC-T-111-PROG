import string


def open_file(filename):
    try:
        word_list = []
        with open(filename, 'r') as data_file:
            data_file = data_file.readlines()
            for line in data_file:
                line = line.split()
                for word in line:
                    stripped = word.strip(string.punctuation).lower()
                    word_list.append(stripped)
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
    search_word = input("Enter search words: ").lower()
    for char in search_word:
        if char == ' ':
            search_word = search_word.split()
        else:
            continue
    for x, word in enumerate(word_list, start=1):
        lower_word = word.lower().strip(string.punctuation)
        search_word_dict.setdefault(lower_word, []).append(x)
    if len(search_word_dict) == 0:
        print("No match.")
    else:
        print("Documents that fit search:", ' '.join(map(str, search_word_dict[search_word])))


def print_documents(word_list):
    header = "<NEW DOCUMENT>."
    header_count = 0
    doc = input("Enter document number: ")
    for x, word in enumerate(word_list):
        if x + 1 == word_list:
            break
        elif word_list[x] and word_list[x + 1] == header:
            header_count += 1


def main():
    filename = input("Document collection: ")
    data_file = open_file(filename)
    file_options(data_file)


main()
