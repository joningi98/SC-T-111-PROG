number_input = input("Please enter a number ")

numbers = [6, 5, 4, 3]

number_input_int = int(number_input)



if number_input_int in numbers:
    print(number_input,"is in the list")
else: 
    print(number_input, "is not in the list")

