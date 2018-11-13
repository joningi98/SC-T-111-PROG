
def get_size_of_table():
    correct_number = True
    while correct_number:
        try:
            size = int(input("Enter the size og the table: "))
            if 1 < size > 8:
                print("Invalid size!")
                continue
            else:
                return size
        except ValueError:
            continue


def print_table(size):
    for y in range(1, size + 1):
        print("{}|".format(y), end='')
        for x in range(1, size + 1):
            print("{}{:<3d}".format("\t\t", (x * y)), end="")
        print("")


def header(size):
    for x in range(1, size + 1):
        print("{}{:>4}".format("\t ", x), end='')
    print("")
    print("{}{}".format("\t\t", '-' * (7*size)))


def main():
    size = get_size_of_table()
    header(size)
    print_table(size)


main()