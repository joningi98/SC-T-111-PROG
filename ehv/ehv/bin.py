b = int("0x30", 16)
a = int("0x39", 16)
for x in range(b, a+1):
    print(bin(x))
    A = (1<<31) >> 28
    b = !(A XOR x)
    b | = !(x XOR 58)
    b | = !(x XOR 59)
