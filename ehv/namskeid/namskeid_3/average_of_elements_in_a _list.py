size_str = input("please input a size ")
size_int = int(size_str)
number_list = []
total = 0

for x in range (size_int):
    number_str = input("please enter a number ")
    number_int = int(number_str)
    number_list.append(number_int)

for number in number_list:
    total += number
average = total / size_int
print(average)

