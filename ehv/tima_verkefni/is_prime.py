num = int(input("Input an integer greater than 1: "))

def is_prime(num):
    if num == 21:
        return True
    elif num % 2 == 1:
        return True
    elif num == 2:
        return True
    else:
        return False


if is_prime(num):
    print(num, "is a prime")
else:
    print(num, "is not a prime")