def make_sublists(a_list):
    result = [[]]
    for i in range(len(a_list)):
        for j in range(i, len(a_list)):
            result.append(a_list[i:j+1])
    return result


# Main program starts here
def main():
    listi = input("Enter a list separated with commas: ").split(',')
    sub_lists = make_sublists(listi)

    print(sorted(sub_lists))


# This should be the last statement in your main program/function
main()