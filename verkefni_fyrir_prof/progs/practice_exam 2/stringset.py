class StringSet(object):
    def __init__(self, text=[]):
        self.__text = text

    def size(self):
        size = 0
        for word in self.__text:
            size += 1
        return size

    def __add__(self, other):
        set1 = [x for x in self.__text]
        set2 = [x for x in other.__text if x not in set1]
        sets = set1 + set2
        word = ""
        for x in sets:
            word += x + " "
        return word

    def at(self, num):
        return self.__text[num]

    def find(self, other):
        my_list = []
        for x in self.__text:
            if x in other:
                my_list.append(x)
        return my_list

    def __repr__(self):
        return self.__text

    def __str__(self):
        line = ''
        for word in self.__text:
            line += word + ' '
        return line


def read_file(doc, file_name):
    text = []
    with open(file_name, "r") as file:
        for line in file.readlines():
            for word in line.split():
                if word not in text:
                    text.append(word.strip())
    new_doc = doc.__init__(text)
    return new_doc


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
