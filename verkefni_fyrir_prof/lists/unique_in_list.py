my_list = []
unique_list = []
size = int(input("Enter the size of the list: "))

for x in range(size):
    num = int(input("Enter a number to put in the list: "))
    my_list.append(num)

for x in my_list:
    if x not in unique_list:
        unique_list.append(x)

print(my_list)
print("The list with no duplicates:", unique_list)
