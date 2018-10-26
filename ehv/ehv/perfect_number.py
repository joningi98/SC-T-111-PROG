top_num = int(input("Upper number for the range: "))
sum = 0

for i in range(1, top_num):
    sum =0
    for j in range(1, i):
        if (i % j == 0):
            sum += j
    if (sum == i):
        print(i)
