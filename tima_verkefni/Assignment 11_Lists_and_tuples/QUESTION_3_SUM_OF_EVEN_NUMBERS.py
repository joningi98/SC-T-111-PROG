def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')

    return a_list

new_list = []


def even_sum(a_list):
    int_list = [int(i) for i in a_list]
    for i in int_list:
        if i % 2 == 0:
            new_list.append(i)
        else:
            pass
    return sum(new_list)


# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))