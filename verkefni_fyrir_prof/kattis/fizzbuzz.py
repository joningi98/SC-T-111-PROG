x, y, n = input().split()

x = int(x)
y = int(y)
n = int(n)


for j in range(1, n + 1):
    if j % x == 0 and j % y == 0:
        print("FizzBuzz")
    elif j % x == 0:
        print("Fizz")
    elif j % y == 0:
        print("Buzz")
    else:
        print(j)