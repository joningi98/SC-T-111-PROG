num = int(input("Input the length of Fibonacci sequence (n>=1): "))

def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)

if num >= 0:
    for x in range(1, num + 1):
        print(f(x), end=" ")