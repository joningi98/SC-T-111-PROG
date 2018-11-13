def get_list():
    my_list = [str(x) for x in input("Enter integers separated with commas: ").split(',')]
    return my_list


def make_sublist(my_list):
    new_list = []
    for x in range(len(my_list) + 1):
        new_list.append(my_list[:x])
        if x in range(len(my_list) + 1):
            new_list.append(my_list[x:])
    print(sorted(new_list))


def main():
    my_list = get_list()
    make_sublist(my_list)


main()
