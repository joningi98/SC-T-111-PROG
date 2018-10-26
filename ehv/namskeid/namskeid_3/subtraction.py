number_1 = input("please enter a number ")
number_2 = input("please enter a number ")

number_1_int = int(number_1)
number_2_int = int(number_2)

def subtraction(a, b):
    result = a - b
    return result

x = subtraction(number_1_int, number_2_int)

print(x)