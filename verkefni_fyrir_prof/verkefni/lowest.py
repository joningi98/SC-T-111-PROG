my_list = [int(x) for x in input("enter numbers plz: ").split()]

lowest_num = my_list[0]
for num in my_list:
    if num < lowest_num:
        lowest_num = num
    else:
        pass
print(lowest_num)
print(my_list)
