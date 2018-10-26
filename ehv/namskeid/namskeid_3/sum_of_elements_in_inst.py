size_str = input("please enter a positive integger ")
size_int = int(size_str)
number_list = []
sum_of_list = 0 

while size_int > 0:
    number_str = input("insert a number ")
    number_int = int(number_str)
    sum_of_list += number_int
    number_list.append(number_int)        
    size_int -= 1
print(sum_of_list)

