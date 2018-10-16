
def make_lists():
    list_1 = [int(x) for x in input("Input a list of integers separated with a comma: ").split(',')]
    list_2 = [int(x) for x in input("Input a list of integers separated with a comma: ").split(',')]
    return list_1, list_2


def options():
    print("1. Intersection\n2. Union\n3. Difference\n4. Quit")
    user_choice = int(input("Set operation: "))
    return user_choice


def make_set_operations(choice, my_list1, my_list2):
    if choice == 1:
        print(set(my_list1).intersection(set(my_list2)))
    if choice == 2:
        print(set(my_list1).union(set(my_list2)))
    if choice == 3:
        print(set(my_list1).difference(set(my_list2)))
    if choice == 4:
        quit()


def main():
    list1, list2 = make_lists()
    print(set(list1))
    print(set(list2))
    while True:
        user_choice = options()
        make_set_operations(user_choice, list1, list2)


main()
