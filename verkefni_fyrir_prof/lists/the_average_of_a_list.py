my_list = []
size = int(input("Enter the size of the list: "))

for x in range(size):
    num = int(input("Enter a number to put in the list: "))
    my_list.append(num)


sum_of_list = sum(my_list)
length_of_list = len(my_list)
average_of_list = sum_of_list / length_of_list

print("the average of the list is", average_of_list)
