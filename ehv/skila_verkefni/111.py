my_str = input("Input a string: ")
index = 0
result = '' # empty string

while index < (len(my_str)-1):
    if my_str[index] < my_str[index+1]:
        result = result + my_str[index]
    else:
        result = result * 2
    index += 1
print(result)