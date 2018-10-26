num_int = int(input("Input a number: ")) # Do not change this line
max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if max_int == 0:
        max_int = num_int
    else:
        if num_int > max_int:
            max_int = num_int   
       


# Fill in the missing code
print("The maximum is", max_int) 
