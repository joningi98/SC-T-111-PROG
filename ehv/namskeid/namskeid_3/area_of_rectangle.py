hight = input("please enter hight ")
lenght = input("please enter length ")

hight_int = int(hight)
length_int = int(lenght)

def area(a, b):
    result = a * b
    return result

result_rectangle = area(hight_int, length_int)

print(result_rectangle)
