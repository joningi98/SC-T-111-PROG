class StringSet:
    def __init__(self):
        self.__text = []

    def add(self, word):
        if word not in self.__text:
            self.__text.append(word)

    def __add__(self, other):
        new_list = StringSet()
        for word in self.__text:
            new_list.add(word)

        for word in other.__text:
            new_list.add(word)

        return new_list

    def size(self):
        return len(self.__text)

    def at(self, other):
        return self.__text[other]

    def find(self, word):
        return word in self.__text

    def __repr__(self):
        return " ".join(self.__text)


def read_file(string_set, filename):
    with open(filename, "r") as file:
        for line in file.readlines():
            for word in line.split():
                string_set.add(word.strip())


def main():
    doc1 = StringSet()
    doc2 = StringSet()
    query = StringSet()

    read_file(doc1, "doc1.txt")
    read_file(doc2, "doc2.txt")

    print("Doc1: ", doc1)
    print("Doc2: ", doc2)

    the_union = doc1 + doc2
    print("Union: ", the_union)

    read_file(query, "query.txt")
    print("Query:", query)

    count = 0
    for i in range(query.size()):
        if the_union.find(query.at(i)):
            count += 1

    print("Query size: ", query.size())
    print("Found in union: ", count)


main()
