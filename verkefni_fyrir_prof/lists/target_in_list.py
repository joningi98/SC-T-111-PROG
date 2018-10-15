my_list = []
size_of_list = int(input("Enter the size of the list: "))

for x in range(size_of_list):
    num = input("enter a number to add to the list: ")
    my_list.append(num)

target = input("What it the target sir? ")
if target in my_list:
    print("The target is in the list")
else:
    print("Sorry sir there is no such target")



