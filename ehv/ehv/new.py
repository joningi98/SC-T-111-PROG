m = int(input("input a number"))
n = int(input("input a numer "))

def computeHCF(a, b):

    if m > n:
        smaller = n
    else:
        smaller = m
    for i in range(1, smaller+1):
        if((m % i == 0) and (n % i == 0)):
            hcf = i
    return hcf

print(computeHCF)