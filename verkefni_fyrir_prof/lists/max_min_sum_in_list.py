my_list = []
size = int(input("Enter the size of the list: "))

for x in range(size):
    num = int(input("Enter a number to put in the list: "))
    my_list.append(num)
print("the highest value in the list is", max(my_list))
print("the lowest value in the list is", min(my_list))
print("the sum of the list is", sum(my_list))
