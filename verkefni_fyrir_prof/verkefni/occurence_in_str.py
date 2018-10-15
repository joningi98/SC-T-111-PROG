a = input("Enter something for a: ")
b = input("Enter something for b: ")

def a_in_b(a, b):
    counter = 0
    for x in range(len(b)-len(a)+1):
        valid = True
        for y in range(len(a)):
            if b[x+y] != a[y]:
                valid = False
                break
        if valid:
            counter += 1
    print(counter)


a_in_b(a, b)
