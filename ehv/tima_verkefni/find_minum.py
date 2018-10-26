first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
def minimum(first,second):
    if first > second:
        return second
    else:
        return first

print("Minimum: ", minimum(first,second))