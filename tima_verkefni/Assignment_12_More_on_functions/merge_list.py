
def merge_lists(list1, list2):
    list3 = list1 + list2
    set_list = set(list3)
    merged_list = list(set_list)
    merged_list.sort()
    return merged_list


# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
