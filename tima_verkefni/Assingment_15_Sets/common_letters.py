

def main():
    first, last = input("Enter name: ").lower().split()
    common_letter_list = get_common_list(first, last)
    print(sorted(common_letter_list))
    print(sorted(get_common_set(first, last)))


def get_common_set(first, last):
    return set(first).intersection(set(last))


def get_common_list(first, last):
    common_letters = []
    for char in first:
        if char in last and char not in common_letters:
            common_letters.append(char)
    return common_letters


main()
