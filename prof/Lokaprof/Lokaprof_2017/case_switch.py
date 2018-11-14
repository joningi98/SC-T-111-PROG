def get_letter():
    letter = input().split()
    return letter


def change_letters(string):
    new_str = []
    for x in string:
        for y in x:
            if y.islower():
                upp = y.upper()
                new_str.append(upp)
            elif y.isupper():
                low = y.lower()
                new_str.append(low)
            else:
                continue
    return new_str


def print_str(string):
    for x in string:
        print(x, end='')


def main():
    my_str = get_letter()
    new_str = change_letters(my_str)
    print_str(new_str)


main()
