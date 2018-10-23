
def get_input():
    name = input("Name: ")
    number = input("Number: ")
    return name, number


def store_in_dict(contacts, name, number):
    contacts[name] = number


def change_to_list_of_tuples(a_dict):
    new_list = []
    for key, val in a_dict.items():
        new_list.append((key, val))
    return new_list


def main():
    contacts = {}
    is_collecting_data = True
    while is_collecting_data:
        name, number = get_input()
        store_in_dict(contacts, name, number)
        more_data = input("More data (y/n)? ")
        if more_data.lower() != 'y':
            is_collecting_data = False

    my_list = change_to_list_of_tuples(contacts)
    print(sorted(my_list))


main()
