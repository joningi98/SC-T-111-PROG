def add_to_dict(a_dict):
    key = input(" Key: ")
    value = int(input("Value: "))
    if key not in a_dict:
        a_dict[key] = value
    else:
        print("Error. Key already exists.")


def remove_from_dict(a_dict):
    key = input(" key to remove: ")
    try:
        a_dict.pop(key)
    except KeyError:
        print("No such key exists in the dictionary.")


def find_key(a_dict):
    key = input(" Key to locate: ")
    if key in a_dict:
        print("Value:  ", a_dict[key])
    else:
        print("Key not found.")


def menu_selection():
    choice = input("Menu: \nadd(a), remove(r), find(f):")
    if choice == 'a' or 'r' or 'f':
        return choice


def execute_selection(choice, a_dict):
    if choice == 'a':
        add_to_dict(a_dict)
    elif choice == 'r':
        remove_from_dict(a_dict)
    elif choice == 'f':
        find_key(a_dict)
    else:
        print(" Invalid choice.")


def dict_to_tuples(a_dict):
    dict_list = []
    for key, val in a_dict.items():
        dict_list.append((key, str(val)))
    return dict_list


# Do not change this main function
def main():
    more = True
    a_dict = {}
    while more:
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'

    dict_list = dict_to_tuples(a_dict)
    print(sorted(dict_list))


main()
