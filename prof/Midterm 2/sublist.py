def the_list():
    my_list = [str(x) for x in input("Enter integers separated with commas:").split(',')]
    return my_list


def make_sublist(the_list):
    new_list = []
    for x in range(len(the_list)+1):
        new_list.append(the_list[:x])
        if x in range(len(the_list)+1):
            new_list.append(the_list[x:])

    return print(sorted(new_list))

# Add thing = [] + 1, 2, 3,
#        if x == len(the_list) - 1:
#            for y in my_list:
#                new_list.append(the_list[x:])
# 1    1 2     123   1234


my_list = the_list()
sublist = make_sublist(my_list)
